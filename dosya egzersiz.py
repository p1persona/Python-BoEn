
import codecs

dosya_olustur=input("dosya adı:")
dosya_new=dosya_olustur+".txt"
veri_gir=input(f"{dosya_new} dosyasına veri ekleyin:")

with codecs.open(dosya_new,"w",encoding="utf-8") as dosya:
    dosya.write(veri_gir)
    soru_sor=input("ekleme yapmak ister misin? e/h")
    if soru_sor=="e":
        open(dosya_new,"a")
        yeni_veri=input("eklemek istediğiniz veri:")
        yeni_veri="\n"+yeni_veri
        dosya.write(yeni_veri)
        print("verileriniz güncellendi...")
    else:
        print("çıkış yapıldı.")

info=open(dosya_new,"r")
a=info.read()
print(a)