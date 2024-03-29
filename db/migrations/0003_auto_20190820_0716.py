# Generated by Django 2.1.11 on 2019-08-20 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20190820_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(max_length=512, verbose_name='居住地址'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='company',
            field=models.CharField(max_length=128, verbose_name='公司'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='graduated',
            field=models.CharField(max_length=128, verbose_name='毕业院校'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=32, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=16, verbose_name='手机'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(max_length=64, verbose_name='职务'),
        ),
    ]
