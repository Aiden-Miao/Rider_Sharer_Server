# Generated by Django 3.0.2 on 2020-02-02 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uper', '0010_auto_20200202_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_ride',
            name='ride',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='uper.Ride'),
        ),
    ]