# Generated by Django 5.1 on 2025-01-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_portfolio_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpreferences',
            name='preferred_method',
            field=models.CharField(choices=[('Email', 'email'), ('Phone', 'phone'), ('LinkedIn', 'linkedin')], default='EMAIL', max_length=20),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='experience_level',
            field=models.CharField(choices=[('Beginner', 'beginner'), ('Junior', 'junior'), ('Mid', 'mid'), ('Senior', 'senior')], default='BEGINNER', max_length=20),
        ),
        migrations.AlterField(
            model_name='specialisation',
            name='name',
            field=models.CharField(choices=[('Python', 'python'), ('Django', 'django'), ('ReactJs', 'reactjs'), ('Html/Css', 'html/css'), ('Java', 'java'), ('Csharp', 'csharp'), ('Javascript', 'javascript')], default='Python', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(choices=[('DevOps', 'devops'), ('AI', 'ai'), ('Frontend', 'frontend'), ('API design', 'API Design'), ('Testing', 'testing'), ('Agile methodologies', 'agile methodologies'), ('Data Visualisation', 'data visualisation'), ('Responsive Design', 'responsive design'), ('Public Speaking', 'public speaking')], max_length=50, unique=True),
        ),
    ]
