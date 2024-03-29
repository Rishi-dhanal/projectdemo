# Generated by Django 5.0.1 on 2024-01-05 04:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=50)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='movie_covers/')),
                ('age_limit', models.CharField(choices=[('All', 'All'), ('Kids', 'Kids')], max_length=10)),
                ('movie_type', models.CharField(choices=[('seasonal', 'Seasonal'), ('single', 'Single')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('age_limit', models.CharField(choices=[('All', 'All'), ('Kids', 'Kids')], max_length=10)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('membership_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mov.membership')),
            ],
        ),
        migrations.CreateModel(
            name='ChildAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mov.register')),
            ],
        ),
        migrations.CreateModel(
            name='AdultAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mov.register')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('register', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mov.register')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mov.user'),
        ),
    ]
