# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-02 15:12
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django_markdown.models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    replaces = [('mainpage', '0001_initial'), ('mainpage', '0002_auto_20160207_1641'), ('mainpage', '0003_auto_20160207_1642'), ('mainpage', '0004_yuki'), ('mainpage', '0005_auto_20160308_1805'), ('mainpage', '0006_auto_20160312_0232'), ('mainpage', '0007_project_file'), ('mainpage', '0008_auto_20160426_1921'), ('mainpage', '0009_auto_20160426_2144'), ('mainpage', '0010_auto_20160427_0113'), ('mainpage', '0011_auto_20160427_1313'), ('mainpage', '0012_auto_20160427_1317'), ('mainpage', '0013_reguser_profile_image'), ('mainpage', '0014_auto_20160427_1926'), ('mainpage', '0015_auto_20160501_1645'), ('mainpage', '0016_auto_20160501_1820')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messsage', django_markdown.models.MarkdownField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idname', models.SlugField()),
                ('name', models.CharField(max_length=40)),
                ('description', django_markdown.models.MarkdownField()),
                ('downloads', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('version', models.CharField(max_length=10)),
                ('ispublic', models.BooleanField()),
                ('thumbnail', easy_thumbnails.fields.ThumbnailerImageField(upload_to='thumbnails/')),
                ('author', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMapType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('name_short', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_upvote', models.BooleanField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='maptype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.ProjectMapType'),
        ),
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.Project'),
        ),
        migrations.AddField(
            model_name='comment',
            name='replyto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainpage.Comment'),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='/thumbnails/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='thumbnails/'),
        ),
        migrations.CreateModel(
            name='RegUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('about', models.TextField(blank=True, default="I'm a metalface", null=True)),
                ('date_registered', models.DateField(auto_now_add=True, default=datetime.datetime(2016, 3, 12, 2, 32, 46, 266133, tzinfo=utc))),
                ('profile_image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='profile_images/')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='file',
            field=models.FileField(upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='ispublic',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='version',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='project',
            name='downloads',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='messsage',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(),
        ),
    ]
