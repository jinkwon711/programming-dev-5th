import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from .validators import *
from .customfield import *

# def URL_validator(self):
#     val=URLValidator(verify_exists=True)
#     try:
#         val(self)
#     except:
#         raise ValidationError
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100,  validators = [MaxLengthValidator(100)] ,verbose_name ="제목")
    content = models.TextField(help_text="Markdown 문법을 써주세요.", validators = [MinLengthValidator(4)])
    tags = models.ManyToManyField('Tag', blank = True)
    lnglat = models.CharField(max_length=50,validators=[lnglat_validator], help_text="경도,위도 포맷으로 입력")
    created_at = models.DateTimeField(default=timezone.now)
    test_field = models.IntegerField(default=10 )
    def __str__(self):
        return "post: "+self.title

class Contact(models.Model):
    name = models.CharField(max_length = 20)
    phone_number = PhoneNumberField()

class Tag(models.Model):
    category = models.CharField(max_length=100, verbose_name = "태그")
    def __str__(self):
        return "tag: "+self.category
# -------------------------------------------------------------------
# class Calculator(object):
#     def __init__(self, base):
#         self.base = base

#     def __call__(self, x, y):



class ZipCode(models.Model):
    zipcode = models.CharField(max_length = 7, validators = [ZipCodeValidator], verbose_name = "우편번호")
    state = models.CharField(max_length = 20 , verbose_name = "시/도" , blank = True)
    city = models.CharField(max_length = 20 , verbose_name = "시/군/" , blank = True)
    roadname = models.CharField(max_length = 10, verbose_name = "도로명" , blank = True)
    def __str__(self):
        return "(우편번호 : "+self.zipcode+") (시/도 : " +self.state+ ") (시/군/구 : "+ self.city +") (도로명 : "+ self.roadname+")"









