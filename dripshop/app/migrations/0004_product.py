# Generated by Django 3.1.7 on 2021-04-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=20)),
                ('price', models.IntegerField(max_length=50)),
                ('image_url', models.CharField(max_length=2000)),
                ('created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
