# Generated by Django 3.2 on 2021-07-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flag',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
