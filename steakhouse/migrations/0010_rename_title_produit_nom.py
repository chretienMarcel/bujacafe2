# Generated by Django 5.0.6 on 2024-09-25 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steakhouse', '0009_remove_commande_pays'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='title',
            new_name='nom',
        ),
    ]
