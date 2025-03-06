# Generated by Django 3.2.25 on 2025-01-20 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=255, null=True)),
                ('content', models.CharField(max_length=1000, null=True)),
                ('image', models.ImageField(null=True, upload_to='productImages/')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
