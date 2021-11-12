# Generated by Django 3.2.5 on 2021-11-10 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20211110_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='link',
            field=models.URLField(null=True),
        ),
    ]