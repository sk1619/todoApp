# Generated by Django 2.2 on 2019-05-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20190507_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='due_date',
            field=models.DateField(),
        ),
    ]
