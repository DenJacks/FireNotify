from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0013_taskarchive"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ReportArchive",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("archived_at", models.DateTimeField(auto_now_add=True)),
                ("report", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="archive_entries", to="api.report")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="report_archives", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name="reportarchive",
            constraint=models.UniqueConstraint(fields=("report", "user"), name="unique_report_archive_per_user"),
        ),
    ]