# Generated by Django 3.0.4 on 2020-04-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a film genre (e.g. sci-fi, comedy)', max_length=50, unique=True, verbose_name='Genre name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]