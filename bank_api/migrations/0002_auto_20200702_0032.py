# Generated by Django 3.0.6 on 2020-07-01 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_name', to='bank_api.banks'),
        ),
    ]