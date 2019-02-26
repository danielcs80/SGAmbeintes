# Generated by Django 2.1.5 on 2019-02-12 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('command', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Actuators',
            },
        ),
        migrations.CreateModel(
            name='Embedded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware', models.CharField(max_length=200)),
                ('firmware', models.FileField(blank=True, upload_to='uploads/')),
                ('location', models.CharField(max_length=100)),
                ('state', models.BooleanField()),
                ('mode', models.CharField(blank=True, choices=[('MASTER', 'MASTER'), ('SLAVE', 'SLAVE')], max_length=6)),
                ('essid', models.CharField(blank=True, max_length=20)),
                ('ip', models.GenericIPAddressField()),
                ('mac', models.GenericIPAddressField()),
                ('mask', models.GenericIPAddressField()),
                ('gateway', models.GenericIPAddressField()),
            ],
            options={
                'verbose_name_plural': 'Embeddeds',
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('rate', models.IntegerField()),
                ('data', models.FloatField()),
                ('fkEmbedded', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgEmbarcados.Embedded')),
            ],
            options={
                'verbose_name_plural': 'Sensors',
            },
        ),
        migrations.AddField(
            model_name='actuator',
            name='fkEmbedded',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgEmbarcados.Embedded'),
        ),
    ]
