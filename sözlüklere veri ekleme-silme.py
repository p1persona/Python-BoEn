
# SÖZLÜKLERE VERİ EKLEME

super_lig={"gs":"63","fb":"62"}
super_lig.setdefault("ts","100")
print(super_lig)

takim_ekle=input("takım giriniz:")
puan_ekle=input("puan giriniz:")

super_lig.setdefault(takim_ekle,puan_ekle)
print(super_lig)


for isim,deger in super_lig.items():
    print(isim,deger)



# SÖZLÜKLERDEN VERİ SİLME

super_lig={"gs":"63","fb":"62"}
super_lig.pop("gs")
print(super_lig)



super_lig.setdefault(takim_ekle,puan_ekle)
print(super_lig)


for i,j in super_lig.items():
    print(isim,deger)


while True:
    takim_ekle=input("takım giriniz:")
    puan_ekle=input("puan giriniz:")
    super_lig.setdefault(takim_ekle,puan_ekle)

    for i,j in super_lig.items():
        print(i,j)

    secim=input("çıkmak ister misiniz e/h:")
    if secim=="e":
        print("çıkış yapıldı.")
        break
    else:
        pass