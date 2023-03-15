from django.db import models


# Create your models here.
class UserSignup(models.Model):
    username = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    pass1 = models.CharField(max_length=50)
    pass2 = models.CharField(max_length=50, null=True)


def __str__(self):
    return self.fname + " " + self.lname


class UserSignin(models.Model):
    username = models.CharField(max_length=50)
    pass1 = models.CharField(max_length=50)
