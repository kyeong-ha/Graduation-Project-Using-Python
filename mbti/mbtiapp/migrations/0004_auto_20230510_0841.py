# Generated by Django 3.2.18 on 2023-05-10 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbtiapp', '0003_mbti'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mbti',
            name='mbti',
        ),
        migrations.AddField(
            model_name='mbti',
            name='id',
            field=models.BigAutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
