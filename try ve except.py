
#  TRY VE EXCEPT : hata yakalama blokları

try:      #hata olma olasılığı olan kod blokları
    sayi=int(input("sayi 1:"))
    sayi2=int(input("sayi 2:"))
    toplam=sayi/sayi2
    print(toplam)

except ZeroDivisionError:    # yakanan hatada çıktı olan açıklama
    print("bir sayı sıfıra bölünemez")

except ValueError:
    print("sayısal veri girin")


except (ZeroDivisionError, ValueError):
    print("hata var...")

