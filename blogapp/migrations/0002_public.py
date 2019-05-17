# Generated by Django 2.1.5 on 2019-05-02 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='public',
            field=models.BooleanField(default=1)
        ),
        migrations.AddField(
            model_name='post',
            name='private_key',
            field=models.CharField(default=None, max_length=32)
        ),
    ]
