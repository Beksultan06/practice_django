# Generated by Django 4.2.4 on 2023-10-05 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_about_title_text_alter_about_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='descriptions_blog',
            field=models.TextField(verbose_name='Описание блога'),
        ),
    ]
