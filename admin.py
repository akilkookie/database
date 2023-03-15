from django.contrib import admin
from .models import UserSignup, UserSignin

# Register your models here.

admin.site.register(UserSignup)
admin.site.register(UserSignin)
