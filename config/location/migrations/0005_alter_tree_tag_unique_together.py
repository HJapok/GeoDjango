# Generated by Django 4.1.4 on 2023-01-09 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_remove_tree_tag_unique_tree_date_combination_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tree_tag',
            unique_together={('Listed_date', 'Tree_id')},
        ),
    ]
