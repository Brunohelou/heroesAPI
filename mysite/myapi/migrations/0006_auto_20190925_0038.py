# Generated by Django 2.2.1 on 2019-09-25 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_auto_20190925_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='heroes',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='heroes',
            field=models.ManyToManyField(related_name='herolist', to='myapi.Hero'),
        ),
    ]