# Generated by Django 2.1.4 on 2019-01-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siscontrol', '0029_auto_20190130_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horarios',
            name='capacitacion',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='capacitacion'),
        ),
    ]