# Generated by Django 3.1.2 on 2020-11-07 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_url_sistem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentOnay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onay_ver', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='onay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.commentonay'),
        ),
    ]
