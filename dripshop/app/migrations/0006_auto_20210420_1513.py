# Generated by Django 3.1.7 on 2021-04-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210420_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prod',
            name='image_url',
        ),
        migrations.AddField(
            model_name='prod',
            name='pic',
            field=models.FileField(null=True, upload_to='static/uploads'),
        ),
    ]
