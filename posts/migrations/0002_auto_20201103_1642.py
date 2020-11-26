# Generated by Django 3.1.2 on 2020-11-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='templates/posts'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='default title', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
    ]
