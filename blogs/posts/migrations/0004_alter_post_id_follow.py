# Generated by Django 5.1.3 on 2024-12-05 04:46

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('49d53d97-84e0-4871-86cb-a6acf106cf0d'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]