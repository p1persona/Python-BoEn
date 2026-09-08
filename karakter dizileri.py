# tüm karakterleri küçük harf yapma

buyuk_harfler = "PERSON".lower()
print(buyuk_harfler)


# tüm karakterleri küçük harf yapma

kucuk_harfler = "person".upper()
print(kucuk_harfler)


# baş harfi buüyük yapma

bas_harf = "person".capitalize()
print(bas_harf)


# tam tersi haline getirme

tam_tersi = "Persona".swapcase()
print(tam_tersi)


# str silme

sil = "+++p+++".strip("+")
print(sil)
sil = " persona".strip()      # boşluğu siler

print(sil.strip())



# istediğimiz elementi koymak
print("zehra","uyar",sep="+")

# sona element ekleme
print("kullanıcı adı",end=":")


adi = "zehra"
soyadi = "uyar"
yasi = 25
print("kişinin adı:{}\nkişinin soyadı:{}\nkişinin yaşı:{}".format(adi,soyadi,yasi))
print(f"kişinin adı:{adi}\nkişinin soyadı:{soyadi}\nkişinin yaşı:{yasi}")