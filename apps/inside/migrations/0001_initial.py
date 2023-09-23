# Generated by Django 4.2.4 on 2023-08-24 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inside',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='ЗАголовка')),
                ('context', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='inside_image', verbose_name='Фотография внутри портфодио')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Настройки внутриннего портфолий',
            },
        ),
    ]