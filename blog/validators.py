import re
import requests
import xmltodict
from django.conf import settings
from django.forms import ValidationError
from django.utils.deconstruct import deconstructible

def lnglat_validator(lnglat):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$',lnglat):
        raise forms.ValidationError('Invalid LngLat Type')

# def min_length_validator(min_length):
#     def wrap(value):
#         if len(value) < min_length:
#             raise ValidationError('{}글자 이상 써주세요'.format(min_length))
#     return wrap
# ->이방법은 마이그레이션으로 동작하지 않는다.
@deconstructible
# 위 장식자는 마이그레이션할때 callable 하게 해주는것. 이미 __call__써서 호출가능하지만 마이그레이션에서는 인식불가로 이걸 써줘야한다고 한다. 그냥 쓸떄는 없이써도됨.
class MinLengthValidator(object):
    def __init__(self, min_length):
        self.min_length = min_length

    def __call__(self, value):
        if len(value) < self.min_length:
            raise ValidationError('{}글자 이상 입력해주세요'.format(self.min_length))


# def max_length_validator(max_length):
#     def wrap(value):
#         if len(value) > max_length:
#             raise ValidationError('{}글자 이하 써주세요'.format(max_length))
#     return wrap
@deconstructible
class MaxLengthValidator(object):
    def __init__(self, max_length):
        self.max_length = max_length

    def __call__(self, value):
        if len(value) > self.max_length:
            raise ValidationError("{}글자 이하로 써주세요".format(self.max_length))

def phone_number_validator(value):
    if not re.match(r'^01[016789][1-9]\d{6,7}$',value):
        raise ValidationError("전화번호를 입력해 주세요")

@deconstructible
class ZipCodeValidator2(object):
    '  우편번호 체계안내 : http://www.koreapost.go.kr/kpost/sub/subpage.jsp?contId=010101040100'
    def __init__(self, is_check_exist = True):
        self.is_check_exist = is_check_exist
    def __call__(self, zip_code):
        if not re.match(r'^\d{5}$', zip_code) and not re.match(r'^\d{3}-?\d{3}$', zip_code):
            raise ValidationError("우편번호는 5자리 혹은 3자리-3자리로 써주시기 바랍니다.")
        # if not len(zip_code) == 5:
        #         z1,z2 = zip_code.split("-")
        #         zip_code = z1+z2

        if self.is_check_exist:
            self.check_exist(zip_code)

    def check_exist(self, zip_code):
        '우체국 open api'
        target = 'postNew'
        if len(zip_code) != 5:
            target = "postRoad"

        params = {
            'regkey' : settings.EPOST_API_KEY,
            'target' : target,
            'query': zip_code.replace("-",""),
        }
        xml = requests.get('http://biz.epost.go.kr/KpostPortal/openapi', params=params).text
        response = xmltodict.parse(xml)
        try:
            error = response['error']
        except KeyError:
            pass
        else:
            raise ValidationError('[{error_code}] {message}'.format(**error))

def ZipCodeValidator(value):
    if not re.match(r'^\d{3}-\d{3}$', value) and not re.match(r'^\d{5}$', value):
        raise ValidationError("구 우편번호는 000-000형식으로, 신 우편번호는 00000형식으로 입력해주세요.")

