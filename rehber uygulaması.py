

# TELEFON REHBERİ UYGULAMASI

# numara ekleme

tel_rehberi=dict()
def tel_no_ekle(x):
    print("---telefon ekleme ekranına hoşgeldiniz---")
    numara_isim_al=input("kayıt edilecek kişi:")
    numara_numara_al=input("numarası:")

    x=tel_rehberi.setdefault(numara_isim_al,numara_numara_al)
    print(f"{numara_isim_al} adlı kişi rehbere eklendi.")

tel_no_ekle(tel_rehberi)



def tel_rehber_goster(x):
    print("rehbere hoşgeldiniz.")
    kisi_sayisi=len(x)
    print(f"rehberinizdeki kişi sayısı:{kisi_sayisi}")


    for i,j in x.items():
        print(i,":","j")
        input("devam edilsin mi?")

tel_no_ekle(tel_rehberi)
tel_rehber_goster(tel_rehberi)


# numara silme

def no_sil(x):
    print("kişi silme ekranına hoşgeldiniz.")
    silinecek_kisi=input("kişiyi yazın:")
    x=tel_rehberi.pop(silinecek_kisi)
    input("devam edilsin mi?")




while True:
    print("hoşgeldiniz")
    print("seçim yapınız:")
    secim_yap=int(input("1-ekle\n2-sil\n3-rehberi gör\n"))

    if secim_yap==1:
        tel_no_ekle(tel_rehberi)

    elif secim_yap==2:
        no_sil(tel_rehberi)
    elif secim_yap==3:
        tel_rehber_goster(tel_rehberi)
    else:
        print("doğru tuşa bas")