# Generated by Django 5.1.7 on 2025-03-24 02:11

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('picture', models.ImageField(upload_to='category_pictures')),
                ('vulnerability', models.CharField(choices=[('very_vulnerable', 'Very Vulnerable'), ('high', 'High'), ('medium', 'Medium'), ('no_need_to_worry', 'No Need to Worry')], max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo_id', models.CharField(blank=True, max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Users.manager')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Users.customer')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Storage.category')),
            ],
        ),
        migrations.CreateModel(
            name='CargoImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cargo_images')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Storage.cargo')),
            ],
        ),
    ]
