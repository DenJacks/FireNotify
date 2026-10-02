from django.db import models
from users.models import User


class Activity(models.Model):

    STATUS_CHOICES = (
        ("SCHEDULED", "Scheduled"),
        ("ONGOING", "Ongoing"),
        ("COMPLETED", "Completed"),
        ("DELAYED", "Delayed"),
        ("FOR_VERIFICATION", "For Verification"),
        ("VERIFIED", "Verified"),
        ("RETURNED", "Returned"),
    )

    title = models.CharField(
        max_length=200
    )

    activity_type = models.CharField(
        max_length=50,
        blank=True,
        default=""
    )

    priority = models.CharField(
        max_length=20,
        default="MEDIUM"
    )

    description = models.TextField(
        blank=True,
        default=""
    )

    activity_date = models.DateField()

    activity_time = models.TimeField(
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=200,
        blank=True,
        default=""
    )

    assigned_personnel = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_activities"
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="SCHEDULED"
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_activities"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title


class ActivitySubmission(models.Model):

    STATUS_CHOICES = (
        ("FOR_VERIFICATION", "For Verification"),
        ("VERIFIED", "Verified"),
        ("RETURNED", "Returned"),
    )

    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="submissions"
    )

    submitted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="activity_submissions"
    )

    accomplishment = models.TextField()

    remarks = models.TextField(
        blank=True,
        default=""
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="FOR_VERIFICATION"
    )

    revision_note = models.TextField(
        blank=True,
        default=""
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.activity.title} - {self.status}"


class SubmissionEvidence(models.Model):

    submission = models.ForeignKey(
        ActivitySubmission,
        on_delete=models.CASCADE,
        related_name="evidence"
    )

    file = models.FileField(
        upload_to="activity_evidence/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Evidence for Submission #{self.submission.id}"


class Task(models.Model):

    STATUS_CHOICES = (
        ("ASSIGNED", "Assigned"),
        ("IN_PROGRESS", "In Progress"),
        ("FOR_VERIFICATION", "For Verification"),
        ("RETURNED", "Returned"),
        ("VERIFIED", "Verified"),
        ("COMPLETED", "Completed"),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    task_type = models.CharField(max_length=80, blank=True, default="General Task")
    priority = models.CharField(max_length=20, default="MEDIUM")
    location = models.CharField(max_length=200, blank=True, default="")
    due_date = models.DateField()
    due_time = models.TimeField(null=True, blank=True)
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tasks",
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_tasks",
    )
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="ASSIGNED")
    progress = models.PositiveSmallIntegerField(default=0)
    accomplishment = models.TextField(blank=True, default="")
    revision_note = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Notification(models.Model):
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications",
    )
    title = models.CharField(max_length=200)
    message = models.TextField()
    notification_type = models.CharField(max_length=50, default="System Alerts")
    source_type = models.CharField(max_length=30, blank=True, default="")
    source_id = models.CharField(max_length=40, blank=True, default="")
    event_key = models.CharField(max_length=160, unique=True, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} for {self.recipient}"


class Report(models.Model):
    title = models.CharField(max_length=200)
    report_type = models.CharField(max_length=80)
    description = models.TextField(blank=True, default="")
    deadline = models.CharField(max_length=120, blank=True, default="")
    assigned_personnel = models.ManyToManyField(
        User,
        through="ReportSubmission",
        through_fields=("report", "personnel"),
        related_name="assigned_reports",
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_reports",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ReportSubmission(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("IN_PROGRESS", "In Progress"),
        ("SUBMITTED", "Submitted"),
        ("FOR_REVIEW", "For Review"),
        ("APPROVED", "Approved"),
        ("RETURNED", "Returned"),
        ("REJECTED", "Rejected"),
    )

    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        related_name="assignments",
    )
    personnel = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="report_assignments",
    )
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    content = models.TextField(blank=True, default="")
    attachment = models.FileField(upload_to="report_evidence/", blank=True, null=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    review_comment = models.TextField(blank=True, default="")
    reviewer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_report_submissions",
    )
    reviewed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["report", "personnel"], name="unique_report_personnel_assignment")
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.report.title} - {self.personnel} ({self.status})"