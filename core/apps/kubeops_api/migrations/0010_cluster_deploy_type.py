# Generated by Django 2.1.2 on 2019-08-06 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0009_auto_20190805_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='deploy_type',
            field=models.CharField(choices=[('MANUAL', 'manual'), ('AUTOMATIC', 'automatic')], default='MANUAL', max_length=128),
        ),
    ]