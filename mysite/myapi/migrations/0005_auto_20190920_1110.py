# Generated by Django 2.2.1 on 2019-09-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_auto_20190920_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='publisher',
            field=models.CharField(choices=[('DC', 'DC'), ('MARVEL', 'Marvel'), ('OTHER', 'Other')], max_length=30, null=True),
        ),
    ]