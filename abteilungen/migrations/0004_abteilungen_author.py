# Generated by Django 4.1.4 on 2023-01-03 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('abteilungen', '0003_alter_abteilungen_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='abteilungen',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='abteiung_author', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]