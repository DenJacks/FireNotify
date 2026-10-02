from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.exceptions import ValidationError

import re

from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import validate_email
from django.utils import timezone

from users.models import User

from .models import (
    Activity,
    ActivitySubmission,
    SubmissionEvidence,
    Task,
    Notification,
    Report,
    ReportSubmission,
)

from .serializers import (
    UserSerializer,
    ActivitySerializer,
    ActivitySubmissionSerializer,
    TaskSerializer,
    NotificationSerializer,
    ReportSerializer,
    ReportSubmissionSerializer,
)


def create_notification(recipient, title, message, notification_type, source_type, source_id, event_key):
    if recipient:
        Notification.objects.get_or_create(
            event_key=event_key,
            defaults={
                "recipient": recipient,
                "title": title,
                "message": message,
                "notification_type": notification_type,
                "source_type": source_type,
                "source_id": str(source_id),
            },
        )


def notify_admins(title, message, notification_type, source_type, source_id, event_key):
    for admin in User.objects.filter(role__iexact="ADMIN"):
        create_notification(
            admin,
            title,
            message,
            notification_type,
            source_type,
            source_id,
            f"{event_key}-{admin.pk}",
        )


NAME_PATTERN = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ]+(?:[ '’-][A-Za-zÀ-ÖØ-öø-ÿ]+)*$")


def is_valid_person_name(value):
    if value is None:
        return False
    return bool(value.strip()) and bool(NAME_PATTERN.fullmatch(value.strip()))


# =========================================================
# GET ALL USERS
# =========================================================

class UserListView(generics.ListAPIView):
    queryset = User.objects.all().order_by("last_name", "first_name")
    serializer_class = UserSerializer


class PendingPersonnelApprovalsView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(role__iexact="PERSONNEL", status="PENDING").order_by("-date_joined")


class PersonnelApprovalActionView(APIView):
    def patch(self, request, pk):
        admin_user = None

        if request.user.is_authenticated and request.user.role == "ADMIN":
            admin_user = request.user
        else:
            admin_id = request.data.get("admin_id")
            admin_email = request.data.get("admin_email")

            if admin_id:
                admin_user = User.objects.filter(pk=admin_id, role__iexact="ADMIN").first()
            elif admin_email:
                admin_user = User.objects.filter(email__iexact=admin_email, role__iexact="ADMIN").first()

        if admin_user is None:
            return Response({"error": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            user = User.objects.get(pk=pk, role__iexact="PERSONNEL")
        except User.DoesNotExist:
            return Response({"error": "Personnel account not found."}, status=status.HTTP_404_NOT_FOUND)

        action = str(request.data.get("action", "")).upper()

        if action == "APPROVE":
            user.status = "APPROVED"
            message = "Personnel account approved."
        elif action == "REJECT":
            user.status = "REJECTED"
            message = "Personnel account rejected."
        else:
            return Response({"error": "Invalid approval action."}, status=status.HTTP_400_BAD_REQUEST)

        user.save(update_fields=["status"])
        return Response({"message": message, "user": UserSerializer(user).data}, status=status.HTTP_200_OK)


# =========================================================
# REGISTER
# =========================================================

class RegisterView(APIView):

    def post(self, request):

        first_name = request.data.get("first_name", "").strip()
        last_name = request.data.get("last_name", "").strip()
        email = request.data.get("email", "").strip().lower()
        username = request.data.get("username", "").strip()
        password = request.data.get("password", "")
        badge_number = request.data.get("badge_number", "").strip()
        rank = str(request.data.get("rank", "")).strip().upper()

        if not is_valid_person_name(first_name):
            return Response({"error": "First name must contain only letters, spaces, hyphens, and apostrophes."}, status=status.HTTP_400_BAD_REQUEST)

        if not is_valid_person_name(last_name):
            return Response({"error": "Last name must contain only letters, spaces, hyphens, and apostrophes."}, status=status.HTTP_400_BAD_REQUEST)

        if not email:
            return Response({"error": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validate_email(email)
        except DjangoValidationError:
            return Response({"error": "Please enter a valid email address."}, status=status.HTTP_400_BAD_REQUEST)

        if not username:
            return Response({"error": "Username is required."}, status=status.HTTP_400_BAD_REQUEST)

        if not badge_number:
            return Response({"error": "Badge number is required."}, status=status.HTTP_400_BAD_REQUEST)

        if not rank:
            return Response({"error": "Rank is required."}, status=status.HTTP_400_BAD_REQUEST)

        if rank not in dict(User.RANK_CHOICES):
            return Response({"error": "Please select a valid BFP rank."}, status=status.HTTP_400_BAD_REQUEST)

        if not password:
            return Response({"error": "Password is required."}, status=status.HTTP_400_BAD_REQUEST)

        if len(password) < 8:
            return Response({"error": "Password must be at least 8 characters long."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"error": "This email is already registered."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username__iexact=username).exists():
            return Response({"error": "This username is already taken."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(badge_number=badge_number).exists():
            return Response({"error": "Badge number is already registered."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            badge_number=badge_number,
            rank=rank,
            role="PERSONNEL",
            status="PENDING",
        )

        serializer = UserSerializer(user)

        return Response(
            {
                "message": "Registration submitted successfully.",
                "user": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


# =========================================================
# LOGIN
# =========================================================

class LoginView(APIView):

    def post(self, request):

        email = request.data.get("email", "").strip().lower()
        password = request.data.get("password", "")

        if not email or not password:
            return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)

        authenticated_user = authenticate(username=user.username, password=password)

        if authenticated_user is None:
            return Response({"error": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, authenticated_user)

        if user.role == "PERSONNEL":
            account_status = str(user.status or "PENDING").upper()
            if account_status == "PENDING":
                return Response({"error": "Your account is still waiting for administrator approval."}, status=status.HTTP_403_FORBIDDEN)
            if account_status == "REJECTED":
                return Response({"error": "Your account registration was rejected. Please contact the administrator."}, status=status.HTTP_403_FORBIDDEN)
            if account_status == "SUSPENDED":
                return Response({"error": "Your account has been suspended. Please contact the administrator."}, status=status.HTTP_403_FORBIDDEN)
            if account_status != "APPROVED":
                return Response({"error": "Your account is not approved for login."}, status=status.HTTP_403_FORBIDDEN)

        if not user.is_active:
            return Response({"error": "This account is inactive."}, status=status.HTTP_403_FORBIDDEN)

        serializer = UserSerializer(user)

        return Response({"message": "Login successful.", "user": serializer.data}, status=status.HTTP_200_OK)


# =========================================================
# ACTIVITIES
# =========================================================

class ActivityListCreateView(
    generics.ListCreateAPIView
):

    queryset = Activity.objects.all().order_by("-created_at")
    serializer_class = ActivitySerializer

    def perform_create(self, serializer):
        activity = serializer.save(status="SCHEDULED")
        assigned = activity.assigned_personnel
        if assigned:
            create_notification(
                assigned,
                "New activity assigned",
                f"{activity.title} has been assigned to you.",
                "Activity Reminders",
                "Activity",
                activity.pk,
                f"activity-assigned-{activity.pk}-{assigned.pk}",
            )
        notify_admins(
            "Activity created",
            f"{activity.title} was created.",
            "Personnel Updates",
            "Activity",
            activity.pk,
            f"activity-created-{activity.pk}",
        )


class ActivityDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def perform_update(self, serializer):
        previous_assignee_id = self.get_object().assigned_personnel_id
        activity = serializer.save()
        if activity.assigned_personnel and activity.assigned_personnel_id != previous_assignee_id:
            create_notification(
                activity.assigned_personnel,
                "New activity assigned",
                f"{activity.title} has been assigned to you.",
                "Activity Reminders",
                "Activity",
                activity.pk,
                f"activity-assigned-{activity.pk}-{activity.assigned_personnel_id}",
            )


# =========================================================
# ACTIVITY SUBMISSIONS
# =========================================================

class ActivitySubmissionListCreateView(
    generics.ListCreateAPIView
):

    queryset = ActivitySubmission.objects.all().order_by(
        "-submitted_at"
    )

    serializer_class = ActivitySubmissionSerializer

    parser_classes = [
        MultiPartParser,
        FormParser,
    ]

    def create(self, request, *args, **kwargs):

        activity_id = request.data.get("activity")
        submitted_by_id = request.data.get("submitted_by")

        accomplishment = request.data.get(
            "accomplishment",
            ""
        )

        remarks = request.data.get(
            "remarks",
            ""
        )

        # ---------------------------------------------
        # VALIDATION
        # ---------------------------------------------

        if not activity_id:
            return Response(
                {
                    "error": "Activity is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not submitted_by_id:
            return Response(
                {
                    "error": "Submitted by is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not accomplishment.strip():
            return Response(
                {
                    "error": "Accomplishment is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ---------------------------------------------
        # FIND ACTIVITY
        # ---------------------------------------------

        try:
            activity = Activity.objects.get(
                id=activity_id
            )

        except Activity.DoesNotExist:
            return Response(
                {
                    "error": "Activity not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # ---------------------------------------------
        # FIND PERSONNEL
        # ---------------------------------------------

        try:
            submitted_by = User.objects.get(
                id=submitted_by_id
            )

        except User.DoesNotExist:
            return Response(
                {
                    "error": "Personnel user not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # ---------------------------------------------
        # CREATE SUBMISSION
        # ---------------------------------------------

        submission = ActivitySubmission.objects.create(
            activity=activity,
            submitted_by=submitted_by,
            accomplishment=accomplishment,
            remarks=remarks,
            status="FOR_VERIFICATION",
        )

        # ---------------------------------------------
        # UPDATE ACTIVITY STATUS
        # ---------------------------------------------

        activity.status = "FOR_VERIFICATION"

        activity.save(
            update_fields=[
                "status",
                "updated_at"
            ]
        )

        # ---------------------------------------------
        # SAVE EVIDENCE FILES
        # ---------------------------------------------

        evidence_files = request.FILES.getlist(
            "evidence"
        )

        for evidence_file in evidence_files:

            SubmissionEvidence.objects.create(
                submission=submission,
                file=evidence_file
            )

        notify_admins(
            "Submission waiting for verification",
            f"{activity.title} was submitted by {submitted_by.get_full_name() or submitted_by.username}.",
            "Reports & Compliance",
            "ActivitySubmission",
            submission.pk,
            f"submission-created-{submission.pk}",
        )

        # ---------------------------------------------
        # RETURN SUBMISSION
        # ---------------------------------------------

        serializer = self.get_serializer(
            submission
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


# =========================================================
# ACTIVITY SUBMISSION DETAIL
# =========================================================

class ActivitySubmissionDetailView(
    generics.RetrieveUpdateAPIView
):

    queryset = ActivitySubmission.objects.all()

    serializer_class = ActivitySubmissionSerializer

    def perform_update(self, serializer):
        previous_status = self.get_object().status
        submission = serializer.save()
        if submission.status != previous_status and submission.submitted_by:
            label = "verified" if submission.status == "VERIFIED" else "returned for revision"
            create_notification(
                submission.submitted_by,
                f"Activity submission {label}",
                f"{submission.activity.title} was {label}. {submission.revision_note}".strip(),
                "Reports & Compliance",
                "ActivitySubmission",
                submission.pk,
                f"submission-{submission.pk}-{submission.status}",
            )


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.select_related("assigned_to", "created_by").order_by("-created_at")
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        if task.assigned_to:
            create_notification(
                task.assigned_to,
                "New task assigned",
                f"{task.title} has been assigned to you.",
                "Task Alerts",
                "Task",
                task.pk,
                f"task-assigned-{task.pk}-{task.assigned_to.pk}",
            )
        notify_admins(
            "Task assigned",
            f"{task.title} was assigned.",
            "Task Alerts",
            "Task",
            task.pk,
            f"task-created-{task.pk}",
        )


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.select_related("assigned_to", "created_by")
    serializer_class = TaskSerializer

    def perform_update(self, serializer):
        previous_status = self.get_object().status
        task = serializer.save()
        if task.status != previous_status and task.assigned_to:
            if task.status == "FOR_VERIFICATION":
                notify_admins(
                    "Task waiting for verification",
                    f"{task.title} was submitted for verification.",
                    "Task Alerts",
                    "Task",
                    task.pk,
                    f"task-submitted-{task.pk}",
                )
            if task.status == "VERIFIED":
                title = "Task verified"
                message = f"{task.title} was verified by Admin."
            elif task.status == "RETURNED":
                title = "Task returned for revision"
                message = f"{task.title}: {task.revision_note}"
            elif task.status == "FOR_VERIFICATION":
                title = "Task submitted for verification"
                message = f"{task.title} is waiting for verification."
            else:
                title = "Task updated"
                message = f"{task.title} status changed to {task.get_status_display()}."
            create_notification(
                task.assigned_to,
                title,
                message,
                "Task Alerts",
                "Task",
                task.pk,
                f"task-{task.pk}-{task.status}",
            )


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        recipient_id = self.request.query_params.get("recipient")
        if not recipient_id:
            return Notification.objects.none()
        try:
            recipient = User.objects.get(pk=recipient_id)
        except User.DoesNotExist:
            return Notification.objects.none()

        today = timezone.localdate()
        is_admin = recipient.role.lower() in {"admin", "administrator"}
        activities = Activity.objects.filter(activity_date__lte=today + timezone.timedelta(days=1))
        tasks = Task.objects.filter(due_date__lte=today + timezone.timedelta(days=1))
        if not is_admin:
            activities = activities.filter(assigned_personnel=recipient)
            tasks = tasks.filter(assigned_to=recipient)

        for activity in activities.exclude(status__in=["COMPLETED", "VERIFIED", "FOR_VERIFICATION"]):
            kind = "overdue" if activity.activity_date < today else "due-today" if activity.activity_date == today else "upcoming"
            create_notification(
                recipient,
                f"Activity {kind.replace('-', ' ')}",
                f"{activity.title} is {kind.replace('-', ' ')}.",
                "Deadline Alerts",
                "Activity",
                activity.pk,
                f"deadline-activity-{activity.pk}-{kind}-{today}-{recipient.pk}",
            )

        for task in tasks.exclude(status__in=["COMPLETED", "VERIFIED", "FOR_VERIFICATION"]):
            kind = "overdue" if task.due_date < today else "due-today" if task.due_date == today else "upcoming"
            create_notification(
                recipient,
                f"Task {kind.replace('-', ' ')}",
                f"{task.title} is {kind.replace('-', ' ')}.",
                "Deadline Alerts",
                "Task",
                task.pk,
                f"deadline-task-{task.pk}-{kind}-{today}-{recipient.pk}",
            )
        return Notification.objects.filter(recipient_id=recipient_id).order_by("-created_at")


class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        recipient_id = self.request.query_params.get("recipient")
        if not recipient_id:
            return Notification.objects.none()
        return Notification.objects.filter(recipient_id=recipient_id)


class MarkAllNotificationsReadView(APIView):
    def post(self, request):
        recipient_id = request.data.get("recipient")
        if not recipient_id:
            return Response({"error": "Recipient is required."}, status=status.HTTP_400_BAD_REQUEST)
        updated = Notification.objects.filter(recipient_id=recipient_id, is_read=False).update(is_read=True)
        return Response({"updated": updated}, status=status.HTTP_200_OK)


class ReportListCreateView(generics.ListCreateAPIView):
    serializer_class = ReportSerializer

    def get_queryset(self):
        return Report.objects.select_related("created_by").prefetch_related(
            "assigned_personnel",
            "assignments__personnel",
            "assignments__reviewer",
        ).order_by("-created_at")

    def perform_create(self, serializer):
        report = serializer.save()
        for assignment in report.assignments.filter(is_active=True).select_related("personnel"):
            create_notification(
                assignment.personnel,
                "New Report Assigned",
                f"{report.title} has been assigned to you.",
                "Reports & Compliance",
                "Report",
                report.pk,
                f"report-assigned-{assignment.pk}",
            )


class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReportSerializer

    def get_queryset(self):
        return Report.objects.select_related("created_by").prefetch_related(
            "assigned_personnel",
            "assignments__personnel",
            "assignments__reviewer",
        )

    def perform_update(self, serializer):
        report = self.get_object()
        previously_active = set(report.assignments.filter(is_active=True).values_list("personnel_id", flat=True))
        report = serializer.save()
        for assignment in report.assignments.filter(is_active=True).exclude(personnel_id__in=previously_active).select_related("personnel"):
            create_notification(
                assignment.personnel,
                "New Report Assigned",
                f"{report.title} has been assigned to you.",
                "Reports & Compliance",
                "Report",
                report.pk,
                f"report-assigned-{assignment.pk}",
            )

    def perform_destroy(self, instance):
        for assignment in instance.assignments.all():
            if assignment.attachment:
                assignment.attachment.delete(save=False)
        instance.delete()


class ReportSubmissionListView(generics.ListAPIView):
    serializer_class = ReportSubmissionSerializer

    def get_queryset(self):
        queryset = ReportSubmission.objects.filter(is_active=True).select_related(
            "report", "personnel", "reviewer"
        ).order_by("-updated_at")
        personnel_id = self.request.query_params.get("personnel")
        if personnel_id:
            return queryset.filter(personnel_id=personnel_id, is_active=True)
        return queryset


class ReportSubmissionDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ReportSubmissionSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_queryset(self):
        queryset = ReportSubmission.objects.select_related("report", "personnel", "reviewer")
        personnel_id = self.request.query_params.get("personnel")
        if personnel_id:
            return queryset.filter(personnel_id=personnel_id, is_active=True)
        return queryset

    def perform_update(self, serializer):
        submission = self.get_object()
        previous_status = submission.status
        requested_status = serializer.validated_data.get("status", previous_status)
        personnel_id = self.request.query_params.get("personnel")

        if personnel_id:
            if str(submission.personnel_id) != str(personnel_id):
                raise ValidationError("This report is not assigned to the current personnel.")
            if requested_status not in {"IN_PROGRESS", "SUBMITTED", "FOR_REVIEW"}:
                raise ValidationError("Personnel cannot set this report status.")
            if requested_status in {"SUBMITTED", "FOR_REVIEW"}:
                content = serializer.validated_data.get("content", submission.content).strip()
                if not content:
                    raise ValidationError({"content": "Report content is required before submission."})
                submission = serializer.save(
                    status="FOR_REVIEW",
                    submitted_at=timezone.now(),
                    review_comment="",
                    reviewer=None,
                    reviewed_at=None,
                )
                if previous_status != "FOR_REVIEW":
                    notify_admins(
                        "Report submitted for review",
                        f"{submission.report.title} was submitted by {submission.personnel.get_full_name() or submission.personnel.username}.",
                        "Reports & Compliance",
                        "ReportSubmission",
                        submission.pk,
                        f"report-submitted-{submission.pk}-{submission.updated_at.timestamp()}",
                    )
                return
            serializer.save(status="IN_PROGRESS")
            return

        if requested_status not in {"APPROVED", "RETURNED", "REJECTED"}:
            raise ValidationError("Admin review status must be Approved, Returned, or Rejected.")

        reviewer_id = serializer.validated_data.get("reviewer")
        submission = serializer.save(
            reviewed_at=timezone.now(),
            reviewer=reviewer_id,
        )
        if submission.status != previous_status:
            label = submission.get_status_display()
            create_notification(
                submission.personnel,
                f"Report {label}",
                f"{submission.report.title} was {label.lower()}. {submission.review_comment}".strip(),
                "Reports & Compliance",
                "ReportSubmission",
                submission.pk,
                f"report-reviewed-{submission.pk}-{submission.status}-{submission.updated_at.timestamp()}",
            )