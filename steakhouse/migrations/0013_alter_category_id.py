# Generated by Django 5.0.6 on 2024-09-25 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steakhouse', '0012_rename_nom_produit_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
