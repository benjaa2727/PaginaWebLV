# Generated by Django 4.2.1 on 2023-06-24 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lavara', '0004_pro'),
    ]

    operations = [
        migrations.CreateModel(
            name='pro1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=0, max_digits=8)),
                ('stock', models.PositiveIntegerField()),
            ],
        ),
    ]
