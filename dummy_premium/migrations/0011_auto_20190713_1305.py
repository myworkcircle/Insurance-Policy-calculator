# Generated by Django 2.0.7 on 2019-07-13 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy_premium', '0010_auto_20190713_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='aadhar',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='pencard',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='photo',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
