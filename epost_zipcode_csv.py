import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "programming.settings")

import django
django.setup()

import csv

CSV_PATH = '/Users/JinHwanKwon/dev/서울특별시.txt'

reader = csv.reader(open(CSV_PATH, 'rt', encoding='cp949'), delimiter ="|")

from blog.models import Zip_Code

columns = next(reader)

zip_code_list =[]

for idx, row in enumerate(reader):

    data = dict(zip(columns, row))
    zip_code = Zip_Code( city=data['시도'], road=data['도로명'], dong=data['법정동명'], gu=data['시군구'], zip_code=data['새우편번호'])
    zip_code_list.append(zip_code)
     # zip_code.save()

print('zip_code size: {}'.format(len(zip_code_list)))
Zip_Code.objects.bulk_create(zip_code_list, 100)
#숫자는 한번에 넣을개수. 1000개 했더니 에러남 너무많이넣어서.