# Generated by Django 3.2.5 on 2021-08-05 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='beers', verbose_name='beer image'),
        ),
    ]
