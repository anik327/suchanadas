# Generated by Django 3.2 on 2021-05-07 12:26

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210430_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='synopsis',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
