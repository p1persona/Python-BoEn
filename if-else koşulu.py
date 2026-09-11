
# IF - ELSE KOŞULU

musteri = 98
if musteri<18:
    print("yaşınız 18 yaşından küçük. sizin yaşınız",musteri)

else:
    print("tebrikler yaşınız 18'den büyük. yaşınız:",musteri)




musteri_yasi = int(input("yaşınız:"))
kabul_yasi = 18
if musteri_yasi<kabul_yasi:
    print("yaş uygun değil:", musteri_yasi)

else:
    print("hoşgeldiniz yaşınız:", musteri_yasi)



sut_miktarı = int(input("süt miktarı:"))
kasar_peyniri_siniri = 11
if sut_miktarı<kasar_peyniri_siniri:
    print("süt miktarı kaşar peyniri için uygun değil", sut_miktarı)
    print("üretmek ihtiyacınız olan süt miktarı:", (kasar_peyniri_siniri-sut_miktarı))

else:
    toplam_uretim = sut_miktarı/kasar_peyniri_siniri
    print(f"toplam üretim:{int(toplam_uretim)}")