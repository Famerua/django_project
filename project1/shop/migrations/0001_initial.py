# Generated by Django 5.0.6 on 2024-06-02 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('desription', models.CharField(default='', max_length=3000)),
                ('price', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
    ]
