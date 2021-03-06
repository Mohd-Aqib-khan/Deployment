# Generated by Django 4.0.3 on 2022-03-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SUBDIVISION', models.CharField(max_length=200)),
                ('YEAR', models.IntegerField()),
                ('JAN', models.FloatField()),
                ('FEB', models.FloatField()),
                ('MAR', models.FloatField()),
                ('APR', models.FloatField()),
                ('MAY', models.FloatField()),
                ('JUN', models.FloatField()),
                ('JUL', models.FloatField()),
                ('AUG', models.FloatField()),
                ('SEP', models.FloatField()),
                ('OCT', models.FloatField()),
                ('NOV', models.FloatField()),
                ('DEC', models.FloatField()),
                ('ANNUAL', models.FloatField()),
                ('Jan_Feb', models.FloatField(db_column='Jan-Feb')),
                ('Mar_May', models.FloatField(db_column='Mar-May')),
                ('Jun_Sep', models.FloatField(db_column='Jun-Sep')),
                ('Oct_Dec', models.FloatField(db_column='Oct-Dec')),
            ],
        ),
    ]
