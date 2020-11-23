# Generated by Django 3.1.3 on 2020-11-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_auto_20201123_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=150),
        ),
    ]