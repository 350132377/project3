# Generated by Django 3.2.3 on 2021-05-29 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='title',
        ),
    ]
