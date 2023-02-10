# Generated by Django 4.1.2 on 2023-02-09 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('announcement', 'announcement'), ('summons', 'summons')], max_length=12)),
                ('date', models.DateField()),
                ('filelink', models.DateField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50, null=True)),
                ('active', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, null=True)),
                ('date', models.DateField()),
                ('bimester', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GradeGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
                ('year', models.IntegerField()),
                ('classroom', models.CharField(max_length=5, null=True)),
                ('children', models.ManyToManyField(to='school.children')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('user_type', models.CharField(choices=[('student', 'student'), ('teacher', 'teacher'), ('parent', 'parent')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='GradesSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.CharField(max_length=5, null=True)),
                ('grade_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.gradegroups')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.subjects')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.users')),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField()),
                ('remarks', models.CharField(max_length=200)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.children')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.events')),
            ],
        ),
        migrations.AddField(
            model_name='gradegroups',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.users'),
        ),
        migrations.AddField(
            model_name='events',
            name='grade_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.gradessubjects'),
        ),
        migrations.CreateModel(
            name='AnnouncementsChildren',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.announcements')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.children')),
                ('grade_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.gradegroups')),
            ],
        ),
        migrations.AddField(
            model_name='announcements',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.users'),
        ),
    ]