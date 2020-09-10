# Generated by Django 3.1.1 on 2020-09-10 01:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirewallRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(max_length=20)),
                ('requestor', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('request_date', models.DateField(auto_now=True)),
                ('expiry_date', models.DateField(blank=True)),
                ('justification', models.TextField(max_length=2000)),
                ('description', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='FirewallRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_ip', models.GenericIPAddressField()),
                ('source_host', models.TextField(max_length=30)),
                ('source_port', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.MinValueValidator(1)])),
                ('destination_ip', models.GenericIPAddressField()),
                ('destination_host', models.TextField(max_length=30)),
                ('destination_port', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.MinValueValidator(1)])),
                ('protocol', models.CharField(choices=[('ICMP', 'ICMP'), ('TCP', 'TCP'), ('UDP', 'UDP')], max_length=4)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firewall.firewallrequest')),
            ],
        ),
    ]