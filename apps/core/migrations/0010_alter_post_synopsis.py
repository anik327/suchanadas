# Generated by Django 3.2 on 2021-05-07 16:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_post_synopsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='synopsis',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=300, null=True),
        ),
    ]
