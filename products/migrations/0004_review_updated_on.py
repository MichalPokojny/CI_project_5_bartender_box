# Generated by Django 3.2.18 on 2023-05-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20230530_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
