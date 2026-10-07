import sqlite3

db=sqlite3.connect("kitaplar.db")

yetki=db.cursor() 
kitap_adi=input("kitap adı:")
kitap_sayfa=input("sayfa sayısı:")
kitap_yili=input("yılı:")


yetki.execute("CREATE TABLE IF NOT EXISTS zehra (isim,sayfa,yıl)") 
yetki.execute('INSERT INTO zehra VALUES ("a","6","2000")')

db.commit()

print(f"kitap eklendi:{kitap_adi}")

db.close()