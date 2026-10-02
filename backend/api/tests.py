from datetime import timedelta

from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase

from users.models import User
from .models import Activity, Notification, Report, ReportSubmission, Task


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
