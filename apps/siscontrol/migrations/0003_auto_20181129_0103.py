# Generated by Django 2.1.3 on 2018-11-29 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siscontrol', '0002_comunicados'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comunicados',
            new_name='comunicados_global',
        ),
        migrations.AlterModelOptions(
            name='comunicados_global',
            options={'ordering': ['-created'], 'verbose_name': 'Comunicado', 'verbose_name_plural': 'Comunicados'},
        ),
    ]