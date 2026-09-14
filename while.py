
# WHILE DÖNGÜLERİ

sayi = 1

while sayi<10:
    print(sayi)
    sayi+=1


# egzersiz

db_ka = "admin" 
db_ps = 1234

while True:
    kullanici_adi=input("lütfen kullanıcı adınızı girin:")
    kullanici_ps=int(input("şifrenizi girin:"))

    if db_ka==kullanici_adi and db_ps==kullanici_ps:
        print("hoşgeldniz:",kullanici_adi)
        break

    elif db_ka!=kullanici_adi and db_ps==kullanici_ps:
        print("kullanıcı adınız hatalı")
    elif db_ka==kullanici_adi and db_ps!=kullanici_ps:
        print("şifreniz hatalı")
        print("şifre değiştirilsin mi? e/h")
        cevap=input()

        if cevap=="e":
            print("şifreniz değiştiriliyor")
            yeni_sifre=int(input("yeni şifrenizi girin:"))
            db_ps=yeni_sifre

    else:
        print("kullanıcı adınız hatalı")