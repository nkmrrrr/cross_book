# Generated by Django 3.1.3 on 2021-06-16 02:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cross_book', '0014_auto_20210616_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='trader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]