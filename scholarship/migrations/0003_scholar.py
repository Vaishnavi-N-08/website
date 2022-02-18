# Generated by Django 3.2.8 on 2021-12-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scholarship', '0002_auto_20211225_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.DecimalField(decimal_places=0, max_digits=10)),
                ('income', models.DecimalField(decimal_places=0, max_digits=10)),
                ('photo', models.ImageField(upload_to='scholar_photo/')),
                ('aadhar', models.FileField(upload_to='schloar_aadhar/')),
                ('income_p', models.FileField(upload_to='schloar_income/')),
            ],
        ),
    ]