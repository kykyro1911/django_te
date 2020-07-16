# Generated by Django 3.0.8 on 2020-07-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_theme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=10)),
                ('u_password', models.CharField(max_length=255)),
                ('u_ticket', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 'testDB',
            },
        ),
    ]
