# Generated by Django 2.2.7 on 2019-12-17 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20191217_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='book',
            new_name='book_title',
        ),
    ]
