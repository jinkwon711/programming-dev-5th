import csv

CSV_PATH = "path"

open(CSV_PATH, encoding="")
# r = read w = write a= append 와 t = text , b = binary 를 조합하여 만든다. rt 는 read,text
reader = csv.reader(open(CSV_PATH, 'rt', encoding = ""), delimiter="")
#필드명 계속보여주기위한것.
columns = next(reader)

for idx, row in enumerate(reader):
    data =  zip(dict(columns, row))
    print(data["필드이름"])
    if idx > 1000:
        break


