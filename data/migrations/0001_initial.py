# Generated by Django 3.2.3 on 2021-07-01 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fees', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('now_attending', models.CharField(choices=[('AWS', 'AWS'), ('DevOps', 'DevOps'), ('React', 'React'), ('Java', 'Java'), ('Python', 'Python'), ('WebDevelopment', 'WebDevelopment')], max_length=100)),
                ('start_date', models.DateField(null=True)),
                ('shared', models.BooleanField(default=False)),
                ('payment', models.CharField(choices=[('full', 'full'), ('half', 'half')], max_length=10)),
                ('course_enrolled', models.ManyToManyField(to='data.Course')),
            ],
        ),
    ]