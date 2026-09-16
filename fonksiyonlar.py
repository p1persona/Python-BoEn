
# FONKSİYONLARA GİRİŞ

def topla():
    a=int(input("ilk sayı:"))
    b=int(input("ikinci sayı:"))

    toplam=a+b
    print(toplam)

topla()


print("*"*25)


ad=input("adınız:")
soyad=input("soyadınız:")
yas=input("yaşınız:")
meslek=input("mesleğiniz:")

print(f"adınız:{ad}\nSoyadınız:{soyad}\nYaşınız:{yas}\nMesleğiniz:{meslek}")
print("*"*25)



def kullanici_bilgileri(ad,soyad,yas,meslek):
    print(f"adınız:{ad}\nSoyadınız:{soyad}\nYaşınız:{yas}\nMesleğiniz:{meslek}")
    print("*"*25)

kullanici_bilgileri("z","u","7","l")
kullanici_bilgileri("q","d","2","ş")


adiniz=input("adınızı yazınız:")
soyadiniz=input("soyadınızı yazınız:")
yasiniz=input("yaşınızı yazınız:")

kullanici_bilgileri(adiniz,soyadiniz,yasiniz)