from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def move_legacy_archives(apps, schema_editor):
    Activity = apps.get_model("api", "Activity")
    ActivityArchive = apps.get_model("api", "ActivityArchive")
    User = apps.get_model(*settings.AUTH_USER_MODEL.split("."))
    first_admin = User.objects.filter(role__iexact="ADMIN").order_by("pk").first()

    for activity in Activity.objects.filter(is_archived=True).select_related("created_by"):
        archive_user = activity.created_by
        if not archive_user or archive_user.role != "ADMIN":
            archive_user = first_admin
        if archive_user:
            ActivityArchive.objects.get_or_create(activity_id=activity.pk, user_id=archive_user.pk)


def restore_legacy_archives(apps, schema_editor):
    Activity = apps.get_model("api", "Activity")
    ActivityArchive = apps.get_model("api", "ActivityArchive")
    archived_activity_ids = ActivityArchive.objects.values_list("activity_id", flat=True).distinct()
    Activity.objects.filter(pk__in=archived_activity_ids).update(is_archived=True)


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0010_activity_is_archived"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ActivityArchive",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("archived_at", models.DateTimeField(auto_now_add=True)),
                ("activity", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="archive_entries", to="api.activity")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="activity_archives", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name="activityarchive",
            constraint=models.UniqueConstraint(fields=("activity", "user"), name="unique_activity_archive_per_user"),
        ),
        migrations.RunPython(move_legacy_archives, restore_legacy_archives),
        migrations.RemoveField(
            model_name="activity",
            name="is_archived",
        ),
    ]