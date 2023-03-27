# Generated by Django 4.1.7 on 2023-03-27 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_abortiondata_state_delete_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('abbreviation', models.CharField(max_length=2)),
            ],
            options={
                'ordering': ('abbreviation',),
            },
        ),
        migrations.AlterField(
            model_name='abortiondata',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='main.state'),
        ),
    ]