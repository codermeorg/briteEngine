# Generated by Django 2.1.7 on 2019-02-19 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('widget', models.CharField(choices=[('date', 'Date'), ('number', 'Number'), ('text', 'Text'), ('enum', 'Predefined Choices')], max_length=10)),
            ],
            options={
                'ordering': ('title',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FieldTypeOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('field_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opts', to='risksman.FieldType')),
            ],
            options={
                'ordering': ('title',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('insurer', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('title',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RiskFieldValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risksman.FieldType')),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='risksman.Risk')),
            ],
        ),
        migrations.CreateModel(
            name='RiskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('opts', models.ManyToManyField(to='risksman.FieldType')),
            ],
            options={
                'ordering': ('title',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='risk',
            name='risk_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risksman.RiskType'),
        ),
    ]
