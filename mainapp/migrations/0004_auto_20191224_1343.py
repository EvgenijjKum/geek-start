# Generated by Django 2.2.2 on 2019-12-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20191224_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
