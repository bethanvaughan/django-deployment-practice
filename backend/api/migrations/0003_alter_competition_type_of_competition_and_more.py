# Generated by Django 4.0.2 on 2022-02-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_name_user_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='type_of_competition',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(),
        ),
    ]
