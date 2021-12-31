# Generated by Django 4.0 on 2021-12-28 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=255)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('timing', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('instagram', models.URLField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('copon_cude', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_category', to='category.category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='palace_city', to='location.city')),
            ],
        ),
    ]
