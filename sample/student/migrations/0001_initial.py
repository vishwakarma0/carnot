# Generated by Django 2.2.15 on 2022-05-25 19:57

from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Title')),
                ('author_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Author Name')),
                ('number_of_pages', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Number of Pages')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_id', models.PositiveIntegerField(blank=True, default=100, null=True, verbose_name='Region ID')),
                ('school', models.CharField(blank=True, max_length=200, null=True, verbose_name='School')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('principal', models.CharField(blank=True, max_length=200, null=True, verbose_name='Principal')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='phone')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='address')),
            ],
            options={
                'verbose_name': 'School',
                'verbose_name_plural': 'Schools',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Last Name')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('gender', model_utils.fields.StatusField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=100, no_check_for_status=True, null=True)),
                ('books', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_book', to='student.Book')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_school', to='student.School')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
    ]
