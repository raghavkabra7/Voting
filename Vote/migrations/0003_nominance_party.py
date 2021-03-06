# Generated by Django 2.2.5 on 2019-10-04 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0002_user_detail_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=100, null=True)),
                ('logo', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Nominance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi_name', models.CharField(max_length=100, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('party_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Vote.Party')),
            ],
        ),
    ]
