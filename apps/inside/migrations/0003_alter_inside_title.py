# Generated by Django 4.2.4 on 2023-08-25 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inside', '0002_alter_inside_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inside',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовка'),
        ),
    ]
