# Generated by Django 4.2.2 on 2023-07-08 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_airvehicles_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airvehicles',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='iha', verbose_name='Resim Upload'),
        ),
    ]
