# Generated by Django 5.1 on 2025-01-25 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_specialisation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpreferences',
            name='preferred_method',
            field=models.CharField(choices=[('email', 'Email'), ('phone', 'Phone'), ('linkedin', 'LinkedIn')], default='EMAIL', max_length=20),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='experience_level',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('junior', 'Junior'), ('mid', 'Mid'), ('senior', 'Senior')], default='BEGINNER', max_length=20),
        ),
        migrations.AlterField(
            model_name='specialisation',
            name='name',
            field=models.CharField(choices=[('python', 'Python'), ('django', 'Django'), ('reactjs', 'ReactJs'), ('html/css', 'Html/Css'), ('java', 'Java'), ('csharp', 'Csharp'), ('javascript', 'Javascript')], default='python', max_length=50, unique=True),
        ),
    ]
