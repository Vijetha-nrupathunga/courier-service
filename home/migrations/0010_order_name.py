# Generated by Django 2.2.5 on 2019-10-12 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20191012_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='name'),
        ),
    ]
