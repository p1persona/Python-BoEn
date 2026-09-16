
# FOR DÖNGÜSÜ

liste = ["zehra", "p1","persona"]

for i in liste:
    print(i)

for sayilar in range(6,20):
    print(sayilar)

deneme = "zehra"

for i in deneme:
    print(i)

for i in deneme:
    print(deneme)




# egzersiz

for i in range(3):
    sifre=input("şifre belirle:")
    if not sifre:
        print("boş alan bırakılmaz")
    elif len(sifre) in range (3,8):
        print("yeni şifreniz:",sifre)
        break
    elif i==2:
        print("şifreyi 3 kere yanlış girdiniz. 5 dk bekleyin")

    else:
        print("şifre 8 den uzun ya da 3 ten kısa")