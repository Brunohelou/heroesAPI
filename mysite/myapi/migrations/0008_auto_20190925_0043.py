# Generated by Django 2.2.1 on 2019-09-25 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_auto_20190925_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='id',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='person', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
