# Generated by Django 2.1.4 on 2019-01-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siscontrol', '0025_auto_20190114_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='turno',
            field=models.CharField(blank=True, choices=[('Ma', 'Matutino'), ('Ve', 'Vespertino'), ('Mi', 'Mixto'), ('Di', 'Director'), ('Pa', 'Paraescolar')], max_length=2, null=True),
        ),
    ]
