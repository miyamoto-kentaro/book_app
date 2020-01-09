# Generated by Django 2.2.7 on 2020-01-02 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_book_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page_content',
            name='page_owner',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(help_text='著者名を記入', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='page_max',
            field=models.IntegerField(help_text='最大ページを記入'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(help_text='本のタイトルを記入', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='version',
            field=models.IntegerField(default=1, help_text='版数を入力'),
        ),
    ]