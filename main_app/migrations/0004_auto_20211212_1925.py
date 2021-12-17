# Generated by Django 3.2.9 on 2021-12-12 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='checked',
            name='pedal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.pedal'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checked',
            name='setup',
            field=models.CharField(choices=[('T', 'Tested'), ('E', 'Effects-Order-Saved'), ('C', 'Cleaned')], default='T', max_length=1),
        ),
    ]
