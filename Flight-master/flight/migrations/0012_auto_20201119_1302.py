# Generated by Django 3.1.2 on 2020-11-19 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0011_auto_20201119_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='flight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='flight.flight'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='flight_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
