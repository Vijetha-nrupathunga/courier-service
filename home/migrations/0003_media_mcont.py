# Generated by Django 2.2.5 on 2019-10-12 05:57

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_user_cont'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='mcont',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='contact'),
        ),
    ]