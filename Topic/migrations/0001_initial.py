# Generated by Django 3.2.3 on 2021-06-04 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Language', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Language.language')),
            ],
        ),
    ]
