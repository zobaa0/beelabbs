# Generated by Django 4.1.1 on 2023-01-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_testimony_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(blank=True, default='siteName', max_length=30, null=True, verbose_name='Site name'),
        ),
    ]
