from datetime import timedelta

from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase

from users.models import User
from .models import Activity, ActivityArchive, ActivityAssignment, ActivitySubmission, Notification, Report, ReportArchive, ReportSubmission, SubmissionEvidence, Task, TaskArchive
from django.core.files.uploadedfile import SimpleUploadedFile


class AuthApprovalFlowTests(APITestCase):
	def test_personnel_registration_is_pending_and_not_approved_immediately(self):
		response = self.client.post(
			reverse("register"),
			{
				"first_name": "Juan",
				"last_name": "Dela Cruz",
				"email": "juan@example.com",
				"username": "juandelacruz",
				"password": "securepass123",
				"badge_number": "BFP-1001",
				"rank": "FO1",
			},
			format="json",
		)
		self.assertEqual(response.status_code, 201)
		user = User.objects.get(email="juan@example.com")
		self.assertEqual(user.role, "PERSONNEL")
		self.assertEqual(user.status, "PENDING")
		self.assertEqual(user.badge_number, "BFP-1001")
		self.assertEqual(user.rank, "FO1")

	def test_registration_rejects_invalid_names_and_accepts_valid_normal_emails(self):
		invalid_cases = [
			{"first_name": "Juan123", "last_name": "Dela Cruz"},
			{"first_name": "Juan@123", "last_name": "Dela Cruz"},
			{"first_name": "12345", "last_name": "Dela Cruz"},
			{"first_name": "!!!Juan", "last_name": "Dela Cruz"},
			{"first_name": "Juan", "last_name": "Dela123"},
		]
		for payload in invalid_cases:
			response = self.client.post(
				reverse("register"),
				{
					"first_name": payload["first_name"],
					"last_name": payload["last_name"],
					"email": "juan@example.com",
					"username": "personnel-unique-1",
					"password": "securepass123",
					"badge_number": "BFP-NAME-1",
					"rank": "FO1",
				},
				format="json",
			)
			self.assertEqual(response.status_code, 400)

		for index, email in enumerate(["juan@gmail.com", "juan@yahoo.com", "juan.outlook@example.com"], start=1):
			response = self.client.post(
				reverse("register"),
				{
					"first_name": "Juan",
					"last_name": "Dela Cruz",
					"email": email,
					"username": f"personnel-{email.split('@')[0]}-{index}",
					"password": "securepass123",
					"badge_number": f"BFP-{email.split('@')[0].upper()}-{index}",
					"rank": "FO1",
				},
				format="json",
			)
			self.assertEqual(response.status_code, 201, msg=f"email {email} should have been accepted")

		for email in ["juan", "juan@", "@example.com"]:
			response = self.client.post(
				reverse("register"),
				{
					"first_name": "Juan",
					"last_name": "Dela Cruz",
					"email": email,
					"username": "invalid-email-user",
					"password": "securepass123",
					"badge_number": "BFP-INVALID-EMAIL",
					"rank": "FO1",
				},
				format="json",
			)
			self.assertEqual(response.status_code, 400)

	def test_pending_rejected_and_suspended_personnel_cannot_login(self):
		pending = User.objects.create_user(
			username="pending-personnel",
			email="pending@example.com",
			password="test-password",
			first_name="Pending",
			last_name="User",
			role="PERSONNEL",
			status="PENDING",
			badge_number="BFP-PENDING-1",
			rank="FO2",
		)
		for status in ["PENDING", "REJECTED", "SUSPENDED"]:
			pending.status = status
			pending.save(update_fields=["status"])
			response = self.client.post(
				reverse("login"),
				{"email": pending.email, "password": "test-password"},
				format="json",
			)
			self.assertNotEqual(response.status_code, 200)
			self.assertIn("account", response.data["error"].lower())

	def test_approved_personnel_can_login_and_admin_remains_approved(self):
		approved = User.objects.create_user(
			username="approved-personnel",
			email="approved@example.com",
			password="test-password",
			first_name="Approved",
			last_name="User",
			role="PERSONNEL",
			status="APPROVED",
			badge_number="BFP-APPROVED-1",
			rank="SFO1",
		)
		login_response = self.client.post(
			reverse("login"),
			{"email": approved.email, "password": "test-password"},
			format="json",
		)
		self.assertEqual(login_response.status_code, 200)
		self.assertEqual(login_response.data["user"]["role"], "PERSONNEL")
		self.assertEqual(login_response.data["user"]["status"], "APPROVED")

		admin = User.objects.create_user(
			username="denjacks12",
			email="denjacks12@example.com",
			password="test-password",
			role="ADMIN",
			status="APPROVED",
		)
		admin_login = self.client.post(
			reverse("login"),
			{"email": admin.email, "password": "test-password"},
			format="json",
		)
		self.assertEqual(admin_login.status_code, 200)
		self.assertEqual(admin_login.data["user"]["role"], "ADMIN")


class PersonnelProfileApiTests(APITestCase):
	def setUp(self):
		self.personnel = User.objects.create_user(
			username="rank-update-personnel",
			email="rank-update@example.com",
			password="test-password",
			first_name="Juan",
			last_name="Dela Cruz",
			role="PERSONNEL",
			status="APPROVED",
			badge_number="BFP-RANK-1",
			rank="FO1",
		)
		self.other_personnel = User.objects.create_user(
			username="other-rank-personnel",
			email="other-rank@example.com",
			password="test-password",
			role="PERSONNEL",
			status="APPROVED",
			badge_number="BFP-RANK-2",
			rank="FO2",
		)

	def test_personnel_can_update_own_rank_for_admin_roster(self):
		self.client.force_authenticate(user=self.personnel)
		response = self.client.patch(
			reverse("personnel-profile-update", args=[self.personnel.pk]),
			{"first_name": "Juan Carlos", "last_name": "Dela Cruz", "rank": "SFO2"},
			format="json",
		)

		self.assertEqual(response.status_code, 200)
		self.personnel.refresh_from_db()
		self.assertEqual(self.personnel.first_name, "Juan Carlos")
		self.assertEqual(self.personnel.last_name, "Dela Cruz")
		self.assertEqual(self.personnel.rank, "SFO2")
		roster_response = self.client.get(reverse("user-list"))
		roster_user = next(user for user in roster_response.data if user["id"] == self.personnel.pk)
		self.assertEqual(roster_user["first_name"], "Juan Carlos")
		self.assertEqual(roster_user["last_name"], "Dela Cruz")
		self.assertEqual(roster_user["rank"], "SFO2")

	def test_login_with_existing_session_accepts_csrf_token(self):
		self.client.enforce_csrf_checks = True
		credentials = {"email": self.personnel.email, "password": "test-password"}
		first_login = self.client.post(reverse("login"), credentials, format="json")
		self.assertEqual(first_login.status_code, 200)

		csrf_token = self.client.cookies["csrftoken"].value
		second_login = self.client.post(
			reverse("login"),
			credentials,
			format="json",
			HTTP_X_CSRFTOKEN=csrf_token,
		)
		self.assertEqual(second_login.status_code, 200)

	def test_profile_accepts_all_supported_rank_codes(self):
		self.client.force_authenticate(user=self.personnel)
		for rank in ["FO1", "FO2", "FO3", "SFO1", "SFO2", "SFO3", "SFO4", "FINSP", "FSINSP", "FCINSP"]:
			response = self.client.patch(
				reverse("personnel-profile-update", args=[self.personnel.pk]),
				{"first_name": "Juan", "last_name": "Dela Cruz", "rank": rank},
				format="json",
			)
			self.assertEqual(response.status_code, 200, msg=f"rank {rank} should be accepted")

	def test_personnel_cannot_update_another_users_rank(self):
		self.client.force_authenticate(user=self.personnel)
		response = self.client.patch(
			reverse("personnel-profile-update", args=[self.other_personnel.pk]),
			{"rank": "SFO2"},
			format="json",
		)

		self.assertEqual(response.status_code, 403)

	def test_profile_rank_must_be_a_valid_bfp_rank(self):
		self.client.force_authenticate(user=self.personnel)
		response = self.client.patch(
			reverse("personnel-profile-update", args=[self.personnel.pk]),
			{"first_name": "Juan", "last_name": "Dela Cruz", "rank": "Chief"},
			format="json",
		)

		self.assertEqual(response.status_code, 400)


class TaskAndNotificationApiTests(APITestCase):
	def setUp(self):
		self.admin = User.objects.create_user(
			username="admin-test",
			email="admin-test@example.com",
			password="test-password",
			role="ADMIN",
			status="APPROVED",
		)
		self.personnel = User.objects.create_user(
			username="personnel-test",
			email="personnel-test@example.com",
			password="test-password",
			role="PERSONNEL",
			status="APPROVED",
			badge_number="BFP-TEST-1",
			rank="FO1",
		)

	def test_new_activity_is_scheduled_even_if_client_sends_completed(self):
		response = self.client.post(
			reverse("activity-list-create"),
			{
				"title": "Smoke alarm inspection",
				"activity_type": "Inspection",
				"activity_date": timezone.localdate().isoformat(),
				"assigned_personnel": self.personnel.pk,
				"created_by": self.admin.pk,
				"status": "COMPLETED",
			},
			format="json",
		)

		self.assertEqual(response.status_code, 201)
		activity = Activity.objects.get(pk=response.data["id"])
		self.assertEqual(activity.status, "SCHEDULED")

	def test_task_assignment_persists_and_notifies_recipient(self):
		response = self.client.post(
			reverse("task-list-create"),
			{
				"title": "Inspect hydrants",
				"description": "Check pressure and accessibility.",
				"priority": "HIGH",
				"due_date": (timezone.localdate() + timedelta(days=2)).isoformat(),
				"assigned_to": self.personnel.pk,
				"created_by": self.admin.pk,
			},
			format="json",
		)

		self.assertEqual(response.status_code, 201)
		task = Task.objects.get(pk=response.data["id"])
		self.assertEqual(task.assigned_to, self.personnel)
		self.assertTrue(Notification.objects.filter(recipient=self.personnel, source_id=str(task.pk)).exists())

	def test_task_archive_is_scoped_and_restore_is_independent(self):
		task = Task.objects.create(
			title="Archive scoped task",
			due_date=timezone.localdate(),
			assigned_to=self.personnel,
			created_by=self.admin,
			accomplishment="Completed inspection.",
			status="FOR_VERIFICATION",
		)
		archive_url = reverse("task-archive-detail", args=[task.pk])

		personnel_archive = self.client.put(archive_url, {"user_id": self.personnel.pk}, format="json")
		self.assertEqual(personnel_archive.status_code, 200)
		self.assertEqual(self.client.get(reverse("task-archive-list"), {"user_id": self.personnel.pk}).data, [task.pk])
		self.assertEqual(self.client.get(reverse("task-archive-list"), {"user_id": self.admin.pk}).data, [])

		admin_archive = self.client.put(archive_url, {"user_id": self.admin.pk}, format="json")
		self.assertEqual(admin_archive.status_code, 200)
		self.assertEqual(self.client.get(reverse("task-archive-list"), {"user_id": self.admin.pk}).data, [task.pk])

		self.client.delete(archive_url, {"user_id": self.personnel.pk}, format="json")
		self.assertEqual(self.client.get(reverse("task-archive-list"), {"user_id": self.personnel.pk}).data, [])
		self.assertEqual(self.client.get(reverse("task-archive-list"), {"user_id": self.admin.pk}).data, [task.pk])
		task.refresh_from_db()
		self.assertEqual(task.status, "FOR_VERIFICATION")
		self.assertEqual(task.accomplishment, "Completed inspection.")

	def test_personnel_task_assignment_removal_keeps_task_record(self):
		task = Task.objects.create(
			title="Remove personnel assignment",
			due_date=timezone.localdate(),
			assigned_to=self.personnel,
			created_by=self.admin,
			accomplishment="Completed inspection.",
			status="FOR_VERIFICATION",
		)
		response = self.client.delete(
			reverse("task-assignment-removal", args=[task.pk]),
			{"user_id": self.personnel.pk},
			format="json",
		)
		self.assertEqual(response.status_code, 200)
		task.refresh_from_db()
		self.assertIsNone(task.assigned_to_id)
		self.assertEqual(task.status, "FOR_VERIFICATION")
		self.assertEqual(task.accomplishment, "Completed inspection.")

	def test_report_assignments_keep_independent_personnel_submissions(self):
		second_personnel = User.objects.create_user(
			username="second-personnel",
			email="second-personnel@example.com",
			password="test-password",
			role="PERSONNEL",
		)
		response = self.client.post(
			reverse("report-list-create"),
			{
				"title": "Fire Safety Inspection Report",
				"report_type": "Inspection Report",
				"description": "Inspect assigned premises.",
				"deadline": "September 30, 2026",
				"assigned_personnel": [self.personnel.pk, second_personnel.pk],
				"assigned_by": self.admin.pk,
			},
			format="json",
		)
		self.assertEqual(response.status_code, 201)
		report = Report.objects.get(pk=response.data["id"])
		self.assertEqual(report.created_by, self.admin)
		self.assertEqual(response.data["assigned_by"], self.admin.pk)
		self.assertEqual(response.data["assigned_by_username"], self.admin.username)
		assignment_data = response.data["assignments"][0]
		self.assertEqual(assignment_data["assigned_by"], self.admin.pk)
		self.assertEqual(assignment_data["assigned_by_username"], self.admin.username)
		self.assertEqual(assignment_data["assigned_by_email"], self.admin.email)
		first = ReportSubmission.objects.get(report=report, personnel=self.personnel)
		second = ReportSubmission.objects.get(report=report, personnel=second_personnel)
		self.assertEqual(first.status, "PENDING")
		self.assertEqual(second.status, "PENDING")
		self.assertTrue(Notification.objects.filter(recipient=self.personnel, source_type="Report").exists())

		listed = self.client.get(reverse("report-submission-list"), {"personnel": self.personnel.pk})
		self.assertEqual(len(listed.data), 1)
		self.assertEqual(listed.data[0]["report_title"], report.title)

		submission_url = f"{reverse('report-submission-detail', args=[first.pk])}?personnel={self.personnel.pk}"
		submitted = self.client.patch(
			submission_url,
			{"status": "FOR_REVIEW", "content": "Inspection completed with no violations."},
			format="json",
		)
		self.assertEqual(submitted.status_code, 200)
		first.refresh_from_db()
		second.refresh_from_db()
		self.assertEqual(first.status, "FOR_REVIEW")
		self.assertEqual(second.status, "PENDING")
		self.assertEqual(second.content, "")

		reviewed = self.client.patch(
			reverse("report-submission-detail", args=[first.pk]),
			{"status": "RETURNED", "review_comment": "Add the inspection date.", "reviewer": self.admin.pk},
			format="json",
		)
		self.assertEqual(reviewed.status_code, 200)
		first.refresh_from_db()
		self.assertEqual(first.status, "RETURNED")
		self.assertEqual(first.review_comment, "Add the inspection date.")

		resubmitted = self.client.patch(
			submission_url,
			{"status": "FOR_REVIEW", "content": "Inspection completed on September 30."},
			format="json",
		)
		self.assertEqual(resubmitted.status_code, 200)
		first.refresh_from_db()
		self.assertEqual(first.status, "FOR_REVIEW")
		self.assertEqual(first.review_comment, "")

		approved = self.client.patch(
			reverse("report-submission-detail", args=[first.pk]),
			{"status": "APPROVED", "review_comment": "Verified.", "reviewer": self.admin.pk},
			format="json",
		)
		self.assertEqual(approved.status_code, 200)
		first.refresh_from_db()
		self.assertEqual(first.status, "APPROVED")
		self.assertEqual(first.review_comment, "Verified.")
		self.assertEqual(first.reviewer, self.admin)

	def test_report_assignment_rejects_admin_as_personnel(self):
		response = self.client.post(
			reverse("report-list-create"),
			{
				"title": "Inspection report",
				"report_type": "Inspection Report",
				"assigned_personnel": [self.admin.pk],
				"created_by": self.admin.pk,
			},
			format="json",
		)
		self.assertEqual(response.status_code, 400)

	def test_notification_read_state_is_recipient_scoped(self):
		notification = Notification.objects.create(
			recipient=self.personnel,
			title="Task assigned",
			message="Inspect hydrants.",
			notification_type="Task Alerts",
		)

		list_response = self.client.get(
			reverse("notification-list"),
			{"recipient": self.personnel.pk},
		)
		self.assertEqual(list_response.status_code, 200)
		self.assertEqual(len(list_response.data), 1)

		update_response = self.client.patch(
			f"{reverse('notification-detail', args=[notification.pk])}?recipient={self.personnel.pk}",
			{"is_read": True},
			format="json",
		)
		self.assertEqual(update_response.status_code, 200)
		notification.refresh_from_db()
		self.assertTrue(notification.is_read)

	def test_verified_past_due_task_does_not_generate_overdue_notice(self):
		task = Task.objects.create(
			title="Completed inspection",
			due_date=timezone.localdate() - timedelta(days=1),
			assigned_to=self.personnel,
			status="VERIFIED",
		)

		response = self.client.get(
			reverse("notification-list"),
			{"recipient": self.personnel.pk},
		)

		self.assertEqual(response.status_code, 200)
		self.assertFalse(Notification.objects.filter(
			recipient=self.personnel,
			source_type="Task",
			source_id=str(task.pk),
			notification_type="Deadline Alerts",
		).exists())


class ActivityArchiveApiTests(APITestCase):
	def setUp(self):
		self.admin = User.objects.create_user(
			username="archive-admin",
			email="archive-admin@example.com",
			password="test-password",
			role="ADMIN",
		)
		self.personnel = User.objects.create_user(
			username="archive-personnel",
			email="archive-personnel@example.com",
			password="test-password",
			role="PERSONNEL",
			badge_number="BFP-ARCHIVE-1",
		)
		self.other_personnel = User.objects.create_user(
			username="other-archive-personnel",
			email="other-archive-personnel@example.com",
			password="test-password",
			role="PERSONNEL",
			badge_number="BFP-ARCHIVE-2",
		)
		self.activity = Activity.objects.create(
			title="Archive scope test",
			activity_date=timezone.localdate(),
			assigned_personnel=self.personnel,
			created_by=self.admin,
		)
		self.submission = ActivitySubmission.objects.create(
			activity=self.activity,
			submitted_by=self.personnel,
			accomplishment="Inspection completed.",
		)
		self.evidence = SubmissionEvidence.objects.create(
			submission=self.submission,
			file=SimpleUploadedFile("evidence.jpg", b"photo-data", content_type="image/jpeg"),
		)

	def archive_url(self):
		return reverse("activity-archive-detail", args=[self.activity.pk])

	def archived_ids(self, user):
		return self.client.get(reverse("activity-archive-list"), {"user_id": user.pk}).data

	def set_archive(self, user, archived):
		method = self.client.put if archived else self.client.delete
		return method(self.archive_url(), {"user_id": user.pk}, format="json")

	def test_personnel_archive_and_restore_are_independent_and_preserve_submissions(self):
		archived = self.set_archive(self.personnel, True)
		self.assertEqual(archived.status_code, 200)
		self.assertEqual(self.archived_ids(self.personnel), [self.activity.pk])
		self.assertEqual(self.archived_ids(self.admin), [])
		self.assertEqual(self.archived_ids(self.other_personnel), [])

		restored = self.set_archive(self.personnel, False)
		self.assertEqual(restored.status_code, 200)
		self.assertEqual(self.archived_ids(self.personnel), [])
		self.assertEqual(self.archived_ids(self.admin), [])
		self.assertTrue(Activity.objects.filter(pk=self.activity.pk).exists())
		self.assertTrue(ActivitySubmission.objects.filter(pk=self.submission.pk).exists())
		self.assertTrue(SubmissionEvidence.objects.filter(pk=self.evidence.pk).exists())

	def test_admin_archive_and_restore_do_not_change_personnel_archive(self):
		self.set_archive(self.personnel, True)
		self.set_archive(self.admin, True)
		self.assertEqual(self.archived_ids(self.admin), [self.activity.pk])
		self.assertEqual(self.archived_ids(self.personnel), [self.activity.pk])

		self.set_archive(self.admin, False)
		self.assertEqual(self.archived_ids(self.admin), [])
		self.assertEqual(self.archived_ids(self.personnel), [self.activity.pk])

	def test_personnel_cannot_archive_an_unassigned_activity(self):
		response = self.client.put(
			reverse("activity-archive-detail", args=[self.activity.pk]),
			{"user_id": self.other_personnel.pk},
			format="json",
		)
		self.assertEqual(response.status_code, 403)
		self.assertFalse(ActivityArchive.objects.filter(activity=self.activity, user=self.other_personnel).exists())

	def test_multiple_admin_assignees_are_returned_and_can_archive_independently(self):
		response = self.client.post(
			reverse("activity-list-create"),
			{
				"title": "Multi-person assignment",
				"activity_date": timezone.localdate().isoformat(),
				"assigned_personnel": self.personnel.pk,
				"assigned_personnel_ids": [self.personnel.pk, self.other_personnel.pk],
				"created_by": self.admin.pk,
			},
			format="json",
		)
		self.assertEqual(response.status_code, 201)
		activity = Activity.objects.get(pk=response.data["id"])
		self.assertEqual(response.data["assigned_personnel_ids"], [self.personnel.pk, self.other_personnel.pk])
		self.assertEqual(
			set(ActivityAssignment.objects.filter(activity=activity).values_list("personnel_id", flat=True)),
			{self.personnel.pk, self.other_personnel.pk},
		)

		archive_response = self.client.put(
			reverse("activity-archive-detail", args=[activity.pk]),
			{"user_id": self.other_personnel.pk},
			format="json",
		)
		self.assertEqual(archive_response.status_code, 200)

	def test_personnel_removal_keeps_activity_submission_and_evidence(self):
		response = self.client.delete(
			reverse("activity-assignment-removal", args=[self.activity.pk]),
			{"user_id": self.personnel.pk},
			format="json",
		)
		self.assertEqual(response.status_code, 200)
		self.assertTrue(Activity.objects.filter(pk=self.activity.pk).exists())
		self.assertIsNone(Activity.objects.get(pk=self.activity.pk).assigned_personnel_id)
		self.assertTrue(ActivitySubmission.objects.filter(pk=self.submission.pk).exists())
		self.assertTrue(SubmissionEvidence.objects.filter(pk=self.evidence.pk).exists())

	def test_personnel_removal_preserves_other_assignees(self):
		ActivityAssignment.objects.create(activity=self.activity, personnel=self.personnel)
		ActivityAssignment.objects.create(activity=self.activity, personnel=self.other_personnel)
		response = self.client.delete(
			reverse("activity-assignment-removal", args=[self.activity.pk]),
			{"user_id": self.personnel.pk},
			format="json",
		)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(
			list(ActivityAssignment.objects.filter(activity=self.activity).values_list("personnel_id", flat=True)),
			[self.other_personnel.pk],
		)
		self.assertEqual(Activity.objects.get(pk=self.activity.pk).assigned_personnel_id, self.other_personnel.pk)


class ReportArchiveApiTests(APITestCase):
	def setUp(self):
		self.admin = User.objects.create_user(
			username="report-archive-admin",
			email="report-archive-admin@example.com",
			password="test-password",
			role="ADMIN",
		)
		self.personnel = User.objects.create_user(
			username="report-archive-personnel",
			email="report-archive-personnel@example.com",
			password="test-password",
			role="PERSONNEL",
			badge_number="BFP-REPORT-ARCHIVE-1",
		)
		self.report = Report.objects.create(
			title="Report archive scope",
			report_type="Inspection Report",
			created_by=self.admin,
		)
		self.assignment = ReportSubmission.objects.create(
			report=self.report,
			personnel=self.personnel,
			status="FOR_REVIEW",
			content="Inspection completed.",
			attachment="report_evidence/preserved.pdf",
		)

	def archive_url(self):
		return reverse("report-archive-detail", args=[self.report.pk])

	def archived_ids(self, user):
		return self.client.get(reverse("report-archive-list"), {"user_id": user.pk}).data

	def test_report_archive_and_restore_are_user_scoped(self):
		personnel_archive = self.client.put(
			self.archive_url(), {"user_id": self.personnel.pk}, format="json"
		)
		self.assertEqual(personnel_archive.status_code, 200)
		self.assertEqual(self.archived_ids(self.personnel), [self.report.pk])
		self.assertEqual(self.archived_ids(self.admin), [])

		admin_archive = self.client.put(
			self.archive_url(), {"user_id": self.admin.pk}, format="json"
		)
		self.assertEqual(admin_archive.status_code, 200)
		self.assertEqual(self.archived_ids(self.admin), [self.report.pk])

		self.client.delete(self.archive_url(), {"user_id": self.admin.pk}, format="json")
		self.assertEqual(self.archived_ids(self.admin), [])
		self.assertEqual(self.archived_ids(self.personnel), [self.report.pk])

		self.client.delete(self.archive_url(), {"user_id": self.personnel.pk}, format="json")
		self.assertEqual(self.archived_ids(self.personnel), [])
		self.assignment.refresh_from_db()
		self.assertTrue(Report.objects.filter(pk=self.report.pk).exists())
		self.assertTrue(self.assignment.is_active)
		self.assertEqual(self.assignment.content, "Inspection completed.")
		self.assertEqual(self.assignment.attachment.name, "report_evidence/preserved.pdf")

	def test_personnel_removal_deactivates_assignment_without_deleting_report_or_submission(self):
		response = self.client.delete(
			reverse("report-assignment-removal", args=[self.assignment.pk]),
			{"user_id": self.personnel.pk},
			format="json",
		)
		self.assertEqual(response.status_code, 200)
		self.assignment.refresh_from_db()
		self.assertFalse(self.assignment.is_active)
		self.assertEqual(self.assignment.status, "FOR_REVIEW")
		self.assertEqual(self.assignment.content, "Inspection completed.")
		self.assertEqual(self.assignment.attachment.name, "report_evidence/preserved.pdf")
		self.assertTrue(Report.objects.filter(pk=self.report.pk).exists())
