# Generated by Django 2.2.9 on 2021-02-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20210215_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
