# Generated by Django 3.1.7 on 2021-04-11 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telemovel',
            name='site',
            field=models.CharField(default='', max_length=8000, unique='false'),
        ),
    ]