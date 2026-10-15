import sqlite3

db=sqlite3.connect("veresiye.db")

yetki=db.cursor()

yetki.execute("CREATE TABLE IF NOT EXISTS kisiler(isim,borc)")

while True:
    print("---VERESİYE DEFTERİNE HOŞGELDİNİZ---")
    sor=input("1-borçlu ekle\n2-borçluları gör\n")
    if sor=="1":
        borclu_isim=input("ismi girin:")
        borc_miktarı=input("borç miktarı:")
        yetki.execute(f"INSERT INTO kisiler{borclu_isim}','{borc_miktarı}'")
        db.commit()
        print(f"işlem tamamlandı, borçlu kişinin adı:{borclu_isim}")
        print("devam edilsin mi?")

    elif sor=="2":
        yetki.execute("SELECT FROM kisiler")
        yazdir=yetki.fetchall()
        say=1
        for i in yazdir:
            print("----borçlu bilgisi----")
            print(f"{say}borçlunun ismi:{i[0]}\nborçlu olduğu miktar:{i[1]}")
            print("devam edilsin mi?")