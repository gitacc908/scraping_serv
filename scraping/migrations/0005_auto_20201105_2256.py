# Generated by Django 3.1.1 on 2020-11-05 16:56

from django.db import migrations, models
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_auto_20201101_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Errors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('data', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
        migrations.AddField(
            model_name='vacancy',
            name='timestamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
