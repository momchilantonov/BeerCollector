# Generated by Django 3.2.5 on 2021-08-02 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30, verbose_name='beer label')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='beer description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='beers/%Y/%m/%d', verbose_name='beer image')),
            ],
        ),
        migrations.CreateModel(
            name='BeerStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=30, null=True, verbose_name='beer type')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BeerStyleLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beer_style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.beerstyle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BeerStyleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('beer_style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.beerstyle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BeerLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.beer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BeerComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.beer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='beer',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.beerstyle'),
        ),
        migrations.AddField(
            model_name='beer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
