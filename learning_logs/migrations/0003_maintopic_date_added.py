# Generated by Django 3.0.4 on 2020-04-14 12:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_maintopic'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintopic',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]