ates=float((input("ateş dereceniz:")))
oksuruk=input("öksürüğünüz var mı?:").lower()
bas_agrisi=input("baş ağrınız var mı?:").lower()
gun=int(input("şikayetleriniz kaç gündür var?:"))

if ates>=39:
    if gun>=3:
        print("hastaneye gidiniz:")
    else:
        print("durum sınırda")

if (ates>=39) and (oksuruk=="e") and (bas_agrisi=="e") and (gun>=3):
    print("acil, durumunuz iyi değil")

elif (oksuruk=="e") or (bas_agrisi=="e") or (gun>=3):
    print("sağlık kuruluşuna gidin")

else:
    print("ateşiniz 39 üstüne çıkar ise hastaneye gidin.")
    print("ateşiniz:",ates)