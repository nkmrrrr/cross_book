# Generated by Django 3.0.3 on 2021-03-30 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cross_book', '0010_auto_20210330_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default='選択してください', max_length=255),
        ),
    ]
