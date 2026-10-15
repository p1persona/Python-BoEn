import sqlite3

db=sqlite3.connect("kitaplar.db")

yetki=db.cursor() 
kitap_adi=input("kitap adı:")
kitap_sayfa=input("sayfa sayısı:")
kitap_yili=input("yılı:")


yetki.execute("CREATE TABLE IF NOT EXISTS zehra (isim,sayfa,yıl)") 
yetki.execute(f'INSERT INTO zehra VALUES("{kitap_adi}","{kitap_sayfa}","{kitap_yili}")')
yetki.execute("SELECT *FROM zehra WHERE yıl='1996'")   # where,0nitelendirir.

yazdir=yetki.fetchall()

for i in yazdir:
    print(f"kitap yılı:{i[2],kitap adı:{i[0]}}")


