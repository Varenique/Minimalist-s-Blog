# Generated by Django 3.1.2 on 2020-11-19 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0007_auto_20201119_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='name_of_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]