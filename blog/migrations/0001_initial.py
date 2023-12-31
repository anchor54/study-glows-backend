# Generated by Django 4.0.4 on 2022-04-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.CharField(blank=True, max_length=256, null=True)),
                ('title', models.CharField(blank=True, max_length=1024, null=True)),
                ('tags', models.CharField(blank=True, max_length=2048, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('alt', models.CharField(blank=True, max_length=1024, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='blog/%Y%m%d')),
                ('published_on', models.DateTimeField(blank=True, null=True)),
                ('publish_status', models.BooleanField(default=False)),
                ('block_status', models.BooleanField(default=False)),
                ('language', models.CharField(blank=True, max_length=512, null=True)),
                ('views', models.PositiveBigIntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=1024, null=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
