
# FINALLY

# try ve except komutlarından sonra en sonunda yazılmasını istediğimiz kod bloğu

import time 

try:
    sayi=int(input("sayi 1:"))
    sayi2=int(input("sayi 2:"))
    toplam=sayi+sayi2
    print(toplam)

except ValueError:
    print("sayı giriniz.")

finally:
    sayac=5
    for i in range(5):
        time.sleep(1)
        print("geri sayım:",sayac)
        sayac-=1
        if sayac==0:
            print("işlem tamamlandı.")