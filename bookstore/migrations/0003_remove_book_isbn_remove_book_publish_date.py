# Generated by Django 4.0.1 on 2022-01-31 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_remove_review_downvotes_remove_review_upvotes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publish_date',
        ),
    ]
