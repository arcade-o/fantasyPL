# Generated by Django 5.1.2 on 2024-11-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FPLUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fpluser',
            name='players',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='fpluser',
            name='startingXI',
            field=models.JSONField(null=True),
        ),
    ]
