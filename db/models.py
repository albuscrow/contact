from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=32, verbose_name='姓名')
    phone = models.CharField(max_length=16, verbose_name='手机')
    company = models.CharField(max_length=128, verbose_name='公司')
    title = models.CharField(max_length=64, verbose_name='职务')
    city = models.CharField(max_length=512, verbose_name='居住地址')
    graduated = models.CharField(max_length=128, verbose_name='毕业院校')
