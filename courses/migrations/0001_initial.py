# Generated by Django 4.2.1 on 2023-05-13 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('thumbnail', models.ImageField(upload_to='files/thumbnail')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('resourse', models.FileField(upload_to='files/resource')),
                ('length', models.IntegerField()),
            ],
        ),
    ]
