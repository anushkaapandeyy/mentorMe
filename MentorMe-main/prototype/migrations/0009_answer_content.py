# Generated by Django 4.0.1 on 2023-04-23 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0008_question_is_answered_question_user_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='content',
            field=models.CharField(default='DEFAULT', max_length=512),
        ),
    ]