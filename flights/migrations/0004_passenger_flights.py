# Generated by Django 5.1.2 on 2024-10-14 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(related_name='passengers', to='flights.flight'),
        ),
    ]
