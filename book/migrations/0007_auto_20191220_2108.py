# Generated by Django 2.2.7 on 2019-12-20 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20191219_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='page_content',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
