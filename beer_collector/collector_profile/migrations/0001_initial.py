# Generated by Django 3.2.5 on 2021-07-22 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectorProfile',
            fields=[
                ('username', models.CharField(max_length=20, verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=20, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=20, verbose_name='last name')),
                ('about', models.CharField(blank=True, max_length=300, verbose_name='about')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/%Y/%m/%d', verbose_name='image')),
                ('is_complete', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.account')),
            ],
        ),
    ]
