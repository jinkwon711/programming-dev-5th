import os
from uuid import uuid4
from django.utils import timezone
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from .validators import *
from .customfield import *
from django.core.urlresolvers import reverse
from django.core.files import File
from django.db.models.signals import pre_save
from programming.pil_image import square_image, thumbnail


# def URL_validator(self):
#     val=URLValidator(verify_exists=True)
#     try:
#         val(self)
#     except:
#         raise ValidationError
# Create your models here.

def random_name_upload_to(instance, filename):
    name = uuid4().hex
    # 랜덤으로 16진수의 32자 숫자 생성.
    extension = os.path.splitext(filename)[-1].lower()
    # 확장자 구하는거 .로 스플릿해서 뒤에서 첫번쨰꺼
    return os.path.join(name[:3], name[3:6], name[6:] + extension)


class Post(models.Model):
    title = models.CharField(max_length=100,  validators = [MaxLengthValidator(100)] ,verbose_name ="제목")
    content = models.TextField(help_text="Markdown 문법을 써주세요.", validators = [MinLengthValidator(4)])
    tags = models.ManyToManyField('Tag', blank = True)
    lnglat = models.CharField(max_length=50,validators=[lnglat_validator], help_text="경도,위도 포맷으로 입력")
    created_at = models.DateTimeField(default=timezone.now)
    test_field = models.IntegerField(default=10 )
    image = models.ImageField(upload_to=random_name_upload_to, blank = True)


    def __str__(self):
        return "post: " + self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])

    @property
    def lat(self):
        return self.lnglat.split(',')[1]

    @property   #변수인것처럼 쓰이면 함수가 호출되게하는것.
    def lng(self):
        return self.lnglat.split(',')[0]
def pre_on_post_save(sender, **kwargs):
    post = kwargs['instance']
    if post.image:

        # post.image = 이미지 저장경로
        # post.image.name = 이미지 파일명 확장자 포
        # post.image.path = 이미지 저장 절대경로
        # post.image.url = 이미지 URL
        # post.image.file = 지정 경로에 대한 파일 오브젝트,
        # post.image.width,height = 이미지 필드만됨.
        max_width = 300
        if post.image.width > max_width or post.image.height > max_width:
            processed_file = thumbnail(post.image.file, max_width, max_width)
            # processed_file = square_image(함post.image.file, max_width)
            post.image.save(post.image.name, File(processed_file))
pre_save.connect(pre_on_post_save, sender=Post)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()
    author = models.CharField(max_length=20)
    Jall = models.ImageField(blank = True)

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



class Zip_Code(models.Model):
    zip_code = models.CharField(max_length =7)
    road = models.CharField(max_length =20)
    dong = models.CharField(max_length =20)
    gu = models.CharField(max_length =20)
    city = models.CharField(max_length =20)






