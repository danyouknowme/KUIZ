# Generated by Django 3.2.7 on 2021-11-19 14:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('correct', models.CharField(max_length=200)),
                ('point', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_topic', models.CharField(max_length=200)),
                ('private', models.BooleanField(default=False)),
                ('password', models.CharField(default='0000', max_length=200)),
                ('detail', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('end_date', models.DateTimeField(default=datetime.datetime(2022, 11, 19, 14, 51, 39, 758671, tzinfo=utc), verbose_name='date end')),
                ('topic', models.CharField(choices=[('', '----------'), ('programming', 'Programming'), ('mathematics', 'Mathematics'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('biology', 'Biology'), ('english', 'English'), ('astronomy', 'Astronomy'), ('social', 'Social'), ('sport', 'Sport'), ('others', 'Others')], default='others', max_length=20)),
                ('exam_duration', models.IntegerField(default=0)),
                ('random_order', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('automate', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(default='', max_length=200)),
                ('correct', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KUIZ.question')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('max_score', models.IntegerField(default=-1)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KUIZ.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KUIZ.quiz'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.TextField(max_length=5000)),
                ('quiz', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='KUIZ.quiz')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KUIZ.question')),
            ],
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KUIZ.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KUIZ.question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KUIZ.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
