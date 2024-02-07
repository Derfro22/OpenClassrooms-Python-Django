# Generated by Django 5.0.1 on 2024-02-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_remove_band_like_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('CD', 'Cd'), ('VL', 'Vinyl'), ('CS', 'Cassette'), ('PO', 'Poster'), ('CL', 'Clothing'), ('OT', 'Other')], default='', max_length=50),
            preserve_default=False,
        ),
    ]