# Generated by Django 3.1.8 on 2022-09-20 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500, null=True)),
                ('show_on_home', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Visa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('documents_required', models.CharField(max_length=1500)),
                ('description', models.CharField(max_length=500, null=True)),
                ('tags', models.ManyToManyField(blank=True, to='visa.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='VisaCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500, null=True)),
                ('price', models.IntegerField(max_length=10)),
                ('visa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visa.visa')),
            ],
        ),
    ]
