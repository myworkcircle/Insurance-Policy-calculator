# Generated by Django 2.0.7 on 2019-06-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy_premium', '0005_auto_20190625_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company1',
            name='value',
            field=models.FloatField(null=True),
        ),
    ]
