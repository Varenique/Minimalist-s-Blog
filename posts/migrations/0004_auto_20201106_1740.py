# Generated by Django 3.1.2 on 2020-11-06 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20201104_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_data',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_text',
            field=models.TextField(verbose_name='Your comment'),
        ),
    ]
