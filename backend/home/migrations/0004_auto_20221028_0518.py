# Generated by Django 2.2.28 on 2022-10-28 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_qasdfgh_sdyuiuytrewq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qasdfgh',
            name='sdyuiuytrewq',
        ),
        migrations.AddField(
            model_name='qasdfgh',
            name='aertAqwerwertyd',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
