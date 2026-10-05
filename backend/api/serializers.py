from rest_framework import serializers

from users.models import User
from .models import (
    Activity,
    ActivityAssignment,
    ActivitySubmission,
    SubmissionEvidence,
    Task,
    Notification,
    Report,
    ReportSubmission,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "role",
            "badge_number",
            "rank",
            "status",
            "is_staff",
            "is_active",
        ]


class ActivitySerializer(serializers.ModelSerializer):
    assigned_personnel_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.filter(role__iexact="PERSONNEL"),
        required=False,
        write_only=True,
        allow_empty=True,
    )

    class Meta:
        model = Activity
        fields = [
            "id",
            "title",
            "activity_type",
            "priority",
            "description",
            "activity_date",
            "activity_time",
            "location",
            "assigned_personnel",
            "assigned_personnel_ids",
            "status",
            "created_by",
            "created_at",
            "updated_at",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        personnel_ids = list(
            instance.personnel_assignments.order_by("personnel_id").values_list("personnel_id", flat=True)
        )
        if not personnel_ids and instance.assigned_personnel_id:
            personnel_ids = [instance.assigned_personnel_id]
        elif instance.assigned_personnel_id in personnel_ids:
            personnel_ids.remove(instance.assigned_personnel_id)
            personnel_ids.insert(0, instance.assigned_personnel_id)
        data["assigned_personnel_ids"] = personnel_ids
        return data

    def _save_personnel_assignments(self, activity, personnel):
        unique_people = list({person.pk: person for person in personnel}.values())
        primary_person = unique_people[0] if unique_people else None
        if activity.assigned_personnel_id != getattr(primary_person, "pk", None):
            activity.assigned_personnel = primary_person
            activity.save(update_fields=["assigned_personnel", "updated_at"])

        ActivityAssignment.objects.filter(activity=activity).delete()
        ActivityAssignment.objects.bulk_create([
            ActivityAssignment(activity=activity, personnel=person)
            for person in unique_people
        ])

    def create(self, validated_data):
        personnel = validated_data.pop("assigned_personnel_ids", None)
        activity = super().create(validated_data)
        if personnel is None:
            personnel = [activity.assigned_personnel] if activity.assigned_personnel else []
        self._save_personnel_assignments(activity, personnel)
        return activity

    def update(self, instance, validated_data):
        personnel = validated_data.pop("assigned_personnel_ids", serializers.empty)
        legacy_assignment_changed = "assigned_personnel" in validated_data
        activity = super().update(instance, validated_data)
        if personnel is not serializers.empty:
            self._save_personnel_assignments(activity, personnel)
        elif legacy_assignment_changed:
            self._save_personnel_assignments(
                activity,
                [activity.assigned_personnel] if activity.assigned_personnel else [],
            )
        return activity


class SubmissionEvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionEvidence
        fields = [
            "id",
            "file",
            "uploaded_at",
        ]


class ActivitySubmissionSerializer(serializers.ModelSerializer):
    evidence = SubmissionEvidenceSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = ActivitySubmission
        fields = [
            "id",
            "activity",
            "submitted_by",
            "accomplishment",
            "remarks",
            "status",
            "revision_note",
            "submitted_at",
            "updated_at",
            "evidence",
        ]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "task_type",
            "priority",
            "location",
            "due_date",
            "due_time",
            "assigned_to",
            "created_by",
            "status",
            "progress",
            "accomplishment",
            "revision_note",
            "created_at",
            "updated_at",
        ]


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "id",
            "recipient",
            "title",
            "message",
            "notification_type",
            "source_type",
            "source_id",
            "is_read",
            "created_at",
        ]
        read_only_fields = ["recipient", "title", "message", "notification_type", "source_type", "source_id", "created_at"]


class ReportSubmissionSerializer(serializers.ModelSerializer):
    personnel_name = serializers.SerializerMethodField()
    report_title = serializers.CharField(source="report.title", read_only=True)
    report_type = serializers.CharField(source="report.report_type", read_only=True)
    report_description = serializers.CharField(source="report.description", read_only=True)
    report_deadline = serializers.CharField(source="report.deadline", read_only=True)
    assigned_by_name = serializers.SerializerMethodField()
    assigned_by = serializers.IntegerField(source="report.created_by_id", read_only=True, allow_null=True)
    assigned_by_username = serializers.SerializerMethodField()
    assigned_by_first_name = serializers.SerializerMethodField()
    assigned_by_last_name = serializers.SerializerMethodField()
    assigned_by_email = serializers.SerializerMethodField()

    class Meta:
        model = ReportSubmission
        fields = [
            "id",
            "report",
            "report_title",
            "report_type",
            "report_description",
            "report_deadline",
            "assigned_by_name",
            "assigned_by",
            "assigned_by_username",
            "assigned_by_first_name",
            "assigned_by_last_name",
            "assigned_by_email",
            "personnel",
            "personnel_name",
            "is_active",
            "status",
            "content",
            "attachment",
            "submitted_at",
            "review_comment",
            "reviewer",
            "reviewed_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["report", "personnel", "created_at", "updated_at"]

    def get_personnel_name(self, submission):
        return submission.personnel.get_full_name() or submission.personnel.username or submission.personnel.email

    def get_assigned_by_name(self, submission):
        creator = submission.report.created_by
        if not creator:
            return "Admin"
        return creator.get_full_name() or creator.username or creator.email

    def _assigned_by_user(self, submission):
        return submission.report.created_by

    def get_assigned_by_username(self, submission):
        creator = self._assigned_by_user(submission)
        return creator.username if creator else ""

    def get_assigned_by_first_name(self, submission):
        creator = self._assigned_by_user(submission)
        return creator.first_name if creator else ""

    def get_assigned_by_last_name(self, submission):
        creator = self._assigned_by_user(submission)
        return creator.last_name if creator else ""

    def get_assigned_by_email(self, submission):
        creator = self._assigned_by_user(submission)
        return creator.email if creator else ""


class ReportSerializer(serializers.ModelSerializer):
    assigned_personnel = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.filter(role__iexact="PERSONNEL"),
        write_only=True,
        required=True,
        allow_empty=False,
    )
    assigned_personnel_ids = serializers.SerializerMethodField()
    assignments = serializers.SerializerMethodField()
    assigned_by = serializers.PrimaryKeyRelatedField(
        source="created_by",
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
    )
    assigned_by_username = serializers.SerializerMethodField()
    assigned_by_first_name = serializers.SerializerMethodField()
    assigned_by_last_name = serializers.SerializerMethodField()
    assigned_by_email = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = [
            "id",
            "title",
            "report_type",
            "description",
            "deadline",
            "assigned_personnel",
            "assigned_personnel_ids",
            "assignments",
            "assigned_by",
            "assigned_by_username",
            "assigned_by_first_name",
            "assigned_by_last_name",
            "assigned_by_email",
            "created_by",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def get_assigned_personnel_ids(self, report):
        return list(report.assignments.filter(is_active=True).values_list("personnel_id", flat=True))

    def get_assignments(self, report):
        assignments = report.assignments.filter(is_active=True).select_related("personnel", "reviewer")
        return ReportSubmissionSerializer(assignments, many=True, context=self.context).data

    def get_assigned_by_username(self, report):
        return report.created_by.username if report.created_by else ""

    def get_assigned_by_first_name(self, report):
        return report.created_by.first_name if report.created_by else ""

    def get_assigned_by_last_name(self, report):
        return report.created_by.last_name if report.created_by else ""

    def get_assigned_by_email(self, report):
        return report.created_by.email if report.created_by else ""

    def create(self, validated_data):
        personnel = validated_data.pop("assigned_personnel")
        report = Report.objects.create(**validated_data)
        ReportSubmission.objects.bulk_create([
            ReportSubmission(report=report, personnel=person)
            for person in personnel
        ])
        return report

    def update(self, instance, validated_data):
        personnel = validated_data.pop("assigned_personnel", None)
        report = super().update(instance, validated_data)
        if personnel is not None:
            requested_ids = {person.pk for person in personnel}
            assignments = {item.personnel_id: item for item in report.assignments.all()}
            for person_id, assignment in assignments.items():
                active = person_id in requested_ids
                if assignment.is_active != active:
                    assignment.is_active = active
                    assignment.save(update_fields=["is_active", "updated_at"])
            for person in personnel:
                if person.pk not in assignments:
                    ReportSubmission.objects.create(report=report, personnel=person)
        return report