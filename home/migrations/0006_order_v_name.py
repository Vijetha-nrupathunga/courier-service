# Generated by Django 2.2.5 on 2019-10-12 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_vehicle_reach'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='v_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.vehicle'),
        ),
    ]
