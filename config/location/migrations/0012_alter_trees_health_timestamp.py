# Generated by Django 4.1.4 on 2023-01-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0011_alter_trees_health_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trees_health',
            name='Timestamp',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]