# Generated by Django 4.1.7 on 2023-04-07 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0002_rename_answers_answer_rename_questions_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Question Title'),
        ),
    ]
