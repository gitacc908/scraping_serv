# Generated by Django 3.1.1 on 2020-11-05 17:53

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import scraping.models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0005_auto_20201105_2256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='errors',
            options={'verbose_name': 'Error', 'verbose_name_plural': 'Errors'},
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_data', jsonfield.fields.JSONField(default=scraping.models.default_urls)),
                ('Language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.language')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.city')),
            ],
            options={
                'unique_together': {('city', 'Language')},
            },
        ),
    ]
