# Generated by Django 3.0.4 on 2020-04-14 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_maintopic_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='main_topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='learning_logs.MainTopic'),
            preserve_default=False,
        ),
    ]
