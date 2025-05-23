# Generated by Django 5.2 on 2025-04-02 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetDatabase',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=32)),
                ('dateOfBirth', models.DateField()),
                ('gender', models.BooleanField()),
                ('breed', models.TextField(max_length=32)),
                ('intakeMethod', models.TextField(max_length=32)),
                ('notes', models.TextField(max_length=256)),
                ('status', models.TextField(max_length=32)),
            ],
        ),
    ]
