# Generated by Django 3.2.3 on 2021-07-01 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_alter_student_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='payment',
            field=models.CharField(choices=[('Full', 'Full'), ('Half', 'Half')], default='Half', max_length=10),
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('complete', models.BooleanField(default=False)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='data.course')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to='data.trainer')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='now_attending',
            field=models.ManyToManyField(related_name='now_attending', to='data.Batch'),
        ),
    ]