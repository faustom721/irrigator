# Generated by Django 4.0.3 on 2022-03-20 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_property_alter_field_unique_together_field_property_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
    ]