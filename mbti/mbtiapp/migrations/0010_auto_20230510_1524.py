# Generated by Django 3.2.18 on 2023-05-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbtiapp', '0009_auto_20230510_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='mbti',
            name='id',
            field=models.BigAutoField(auto_created=True, default=4, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mbti',
            name='mbti',
            field=models.CharField(max_length=200),
        ),
    ]