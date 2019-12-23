# Generated by Django 2.2.2 on 2019-12-22 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketslot',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='количество'),
        ),
        migrations.AlterField(
            model_name='basketslot',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basketslot', to=settings.AUTH_USER_MODEL),
        ),
    ]
