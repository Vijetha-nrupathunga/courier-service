# Generated by Django 2.2.5 on 2019-10-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='accept/reject'),
        ),
    ]
