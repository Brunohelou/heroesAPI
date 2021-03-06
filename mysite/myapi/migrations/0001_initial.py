# Generated by Django 2.2.1 on 2019-09-26 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('alias', models.CharField(max_length=60)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('description', models.TextField(null=True)),
                ('publisher', models.CharField(choices=[('DC', 'DC'), ('MARVEL', 'Marvel'), ('OTHER', 'Other')], max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.CharField(default='', max_length=100)),
                ('heroes', models.ManyToManyField(related_name='herolist', to='myapi.Hero')),
            ],
        ),
    ]
