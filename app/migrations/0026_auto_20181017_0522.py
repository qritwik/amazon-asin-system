# Generated by Django 2.0.2 on 2018-10-17 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_olddetailamazon_old_from_manufacture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='olddetailamazon',
            old_name='old_from_manufacture',
            new_name='old_from_manufacture_h',
        ),
        migrations.AddField(
            model_name='olddetailamazon',
            name='old_from_manufacture_p',
            field=models.CharField(blank=True, max_length=1000000, null=True),
        ),
    ]
