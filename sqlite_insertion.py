

import csv, sqlite3
conn = sqlite3.connect("db.sqlite3")
curs = conn.cursor()
curs.execute("CREATE TABLE PCFC (id INTEGER PRIMARY KEY, type INTEGER, term TEXT, definition TEXT);")
reader = csv.reader(open('newzipcode_seoul.csv'), delimiter=',')
for row in reader:
    to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8")]
    curs.execute("INSERT INTO PCFC (type, term, definition) VALUES (?, ?, ?);", to_db)
conn.commit()