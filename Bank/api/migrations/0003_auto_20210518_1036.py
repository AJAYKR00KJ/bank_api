# Generated by Django 3.2.3 on 2021-05-18 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210518_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchinfo',
            name='address',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='branchinfo',
            name='bank_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='branchinfo',
            name='branch',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='branchinfo',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='branchinfo',
            name='district',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='branchinfo',
            name='ifsc',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='branchinfo',
            name='state',
            field=models.CharField(max_length=200),
        ),
    ]
