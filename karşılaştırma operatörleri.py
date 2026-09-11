
# KARŞILAŞTIRMA OPERATÖRLERİ

# eşittir
deneme = 5 == 5
print(deneme)

deneme1 = 6 == 5
print(deneme1)

db = 1234
kullanici_sifre = int(input("şifrenizi girin:"))
kontrol = db ==kullanici_sifre
print(kontrol)



#eşit değildir
deneme2 = 4 != 3
print(deneme2)

db = 1234
kb = 12345
kontrol1 = db !=kb
print(kontrol1)



#küçüktür
deneme3 = 1<3
print(deneme3)

yas = 17
kontrol2 = yas<17
print(kontrol2)



#küçük ya da eşittir
yas1 = 17
kontrol3 = yas<=17
print(kontrol3)



# büyüktür
yas2 = 17
kontrol4 = yas2>17
print(kontrol4)



# büyük ve ya eşittir
yas3 = 17
kontrol5 = yas=>17
print(kontrol5)



liste = [1,2,3,4]
liste2 = [1,2,3,4,5]
kontrol6 = len(liste) < len(liste2)
print(kontrol6)