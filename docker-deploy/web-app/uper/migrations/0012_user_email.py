# Generated by Django 3.0.2 on 2020-02-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uper', '0011_auto_20200202_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
