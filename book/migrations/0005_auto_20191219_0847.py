# Generated by Django 2.2.7 on 2019-12-18 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20191217_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='book_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book'),
        ),
        migrations.CreateModel(
            name='Page_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_owner', models.CharField(max_length=100)),
                ('content_title', models.CharField(max_length=100)),
                ('formula_number', models.CharField(max_length=100)),
                ('line', models.IntegerField()),
                ('formula_or_sentence', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
                ('page_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book.Page')),
            ],
        ),
    ]