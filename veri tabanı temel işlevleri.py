
import sqlite3

db=sqlite3.connect("kitaplar.db")
yetki=db.cursor()   # imleç. db üzerinde işlem yapmak için.

yetki.execute("CREATE TABLE IF NOT EXISTS zehra (isim,sayfa,yıl)")  # değişiklik yapmak için.
yetki.execute('INSERT INTO zehra VALUES ("a","6","2000")')

db.commit()

db.close()