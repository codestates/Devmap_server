# Generated by Django 3.1.4 on 2020-12-04 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='roadmap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
                ('frontback', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('commentsid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roadmap.comments')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roadmap.users')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='roadmapid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roadmap.roadmap'),
        ),
        migrations.AddField(
            model_name='comments',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roadmap.users'),
        ),
    ]
