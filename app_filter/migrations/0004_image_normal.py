# Generated by Django 3.0.3 on 2020-04-02 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_filter', '0003_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_Normal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
    ]