# Generated by Django 4.0.3 on 2022-03-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Like Count'),
        ),
    ]
