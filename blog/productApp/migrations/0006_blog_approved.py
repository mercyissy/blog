# Generated by Django 3.2.25 on 2025-02-28 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0005_blog_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
