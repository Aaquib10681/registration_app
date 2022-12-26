# Generated by Django 4.1.4 on 2022-12-26 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('info', models.CharField(blank=True, max_length=8192, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerInforation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('son_of', models.CharField(blank=True, max_length=512, null=True)),
                ('address', models.CharField(blank=True, max_length=1024, null=True)),
                ('dob', models.DateField(max_length=8)),
                ('age', models.CharField(blank=True, max_length=8, null=True)),
                ('qulification', models.CharField(blank=True, max_length=64, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_category', to='games.category')),
            ],
        ),
    ]