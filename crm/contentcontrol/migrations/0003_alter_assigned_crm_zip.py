# Generated by Django 4.2 on 2023-04-21 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcontrol', '0002_assigned_crm_unassigned_crm_delete_crm_items_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigned_crm',
            name='zip',
            field=models.IntegerField(),
        ),
    ]
