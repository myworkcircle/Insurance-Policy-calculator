# Generated by Django 2.0.7 on 2019-07-13 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy_premium', '0009_dummy_documents'),
    ]

    operations = [
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='dummy',
            name='documents',
        ),
    ]