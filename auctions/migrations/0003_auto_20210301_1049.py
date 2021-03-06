# Generated by Django 3.1.6 on 2021-03-01 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_category_comment_listing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='image_url',
            new_name='imageURL',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='currentBid',
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.CharField(max_length=1024),
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.AddField(
            model_name='bids',
            name='acution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
        migrations.AddField(
            model_name='bids',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids_makers', to=settings.AUTH_USER_MODEL),
        ),
    ]
