from django.db import models


# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=32, verbose_name='Name')
    email = models.EmailField(verbose_name="Email")


class UserInfo(models.Model):
    user_name = models.CharField(max_length=32, verbose_name='Name')
    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return self.user_name
