# Generated by Django 4.0.2 on 2022-02-25 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_rename_book_category_booklist_book_categorys'),
    ]

    operations = [
        migrations.AddField(
            model_name='booklist',
            name='book_image',
            field=models.ImageField(default=1, upload_to='book_img'),
            preserve_default=False,
        ),
    ]
