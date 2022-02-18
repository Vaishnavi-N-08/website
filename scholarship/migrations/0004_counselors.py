# Generated by Django 3.2.8 on 2022-01-24 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0003_scholar'),
    ]

    operations = [
        migrations.CreateModel(
            name='counselors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=150)),
                ('number', models.DecimalField(decimal_places=0, max_digits=10)),
                ('course', models.CharField(max_length=100)),
                ('proof', models.FileField(upload_to='course_proof/')),
                ('address', models.TextField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]