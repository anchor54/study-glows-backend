# Generated by Django 4.0.4 on 2022-06-26 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_series', '0006_alter_question_options_remove_question_order_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestsetQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('order', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('publish', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.RemoveField(
            model_name='question',
            name='publish',
        ),
        migrations.AddField(
            model_name='testset',
            name='questions',
            field=models.ManyToManyField(blank=True, through='test_series.TestsetQuestion', to='test_series.question'),
        ),
        migrations.AddField(
            model_name='testsetquestion',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_series.question'),
        ),
        migrations.AddField(
            model_name='testsetquestion',
            name='testset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_series.testset'),
        ),
    ]
