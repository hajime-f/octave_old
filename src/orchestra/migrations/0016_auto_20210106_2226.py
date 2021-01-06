# Generated by Django 3.1.4 on 2021-01-06 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orchestra', '0015_orchestra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orchestra',
            name='admin_users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orchestra', to=settings.AUTH_USER_MODEL, verbose_name='管理者'),
        ),
    ]
