# Generated by Django 2.2.6 on 2019-12-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Latest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(null=True)),
                ('blog_url', models.URLField()),
                ('image', models.TextField()),
                ('featured', models.BooleanField()),
            ],
        ),
    ]
