from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_reportsubmission_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]