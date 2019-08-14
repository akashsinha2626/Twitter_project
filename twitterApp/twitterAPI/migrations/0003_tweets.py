# Generated by Django 2.1.7 on 2019-08-13 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('twitterAPI', '0002_delete_tweets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_at', models.CharField(max_length=45)),
                ('tweet', models.TextField()),
                ('username', models.CharField(max_length=100)),
                ('retweet_count', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
            ],
        ),
    ]
