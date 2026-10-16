import sqlite3

db=sqlite3.connect("kitaplar.db")

yetki=db.cursor() 
kitap_adi=input("kitap adı:")
kitap_sayfa=input("sayfa sayısı:")
kitap_yili=input("yılı:")


yetki.execute("CREATE TABLE IF NOT EXISTS zehra (isim,sayfa,yıl)") 
yetki.execute(f'INSERT INTO zehra VALUES("{kitap_adi}","{kitap_sayfa}","{kitap_yili}")')
yetki.execute("SELECT *FROM zehra")

yazdir=yetki.fetchall()       # tüm veri tabanına ulaşır.

say=1
for i in yazdir:
    print("kitap bilgisi")
    print(f"{say}kitap adı:{i[0]}\nsayfa sayısı:{i[1]}\nyılı:{i[2]}")
    say+=1

db.commit()




yazdir=yetki.fetchmany()     # içinden herhangi bir sayıda veri çeker.

for i in yazdir:
    print(i)






#print(f"kitap eklendi:{kitap_adi}")

db.close()