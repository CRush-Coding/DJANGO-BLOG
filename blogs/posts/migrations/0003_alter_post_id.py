# Generated by Django 5.1.3 on 2024-12-05 03:56

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_id_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('47375c1e-d264-4637-93db-855b9ce74313'), editable=False, primary_key=True, serialize=False),
        ),
    ]
