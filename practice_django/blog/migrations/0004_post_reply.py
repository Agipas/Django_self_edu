# Generated by Django 4.1.5 on 2023-01-24 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_likes_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_ok', to='blog.post'),
        ),
    ]
