# Generated by Django 3.1 on 2020-09-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200903_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
