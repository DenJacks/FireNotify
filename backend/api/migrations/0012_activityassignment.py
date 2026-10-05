from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def copy_existing_assignments(apps, schema_editor):
    Activity = apps.get_model("api", "Activity")
    ActivityAssignment = apps.get_model("api", "ActivityAssignment")
    assignments = [
        ActivityAssignment(activity_id=activity_id, personnel_id=personnel_id)
        for activity_id, personnel_id in Activity.objects.exclude(
            assigned_personnel__isnull=True
        ).values_list("id", "assigned_personnel_id")
    ]
    ActivityAssignment.objects.bulk_create(assignments, ignore_conflicts=True)


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0011_activityarchive_remove_activity_is_archived"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ActivityAssignment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("activity", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="personnel_assignments", to="api.activity")),
                ("personnel", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="activity_assignments", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name="activityassignment",
            constraint=models.UniqueConstraint(fields=("activity", "personnel"), name="unique_activity_personnel_assignment"),
        ),
        migrations.RunPython(copy_existing_assignments, migrations.RunPython.noop),
    ]