
# DOSYA BAŞINA VERİ EKLEME 


import codecs

with codecs.open("deneme.txt","r+",encoding="utf=8") as dosya:
    # r+ = hem yazma hem okuma metodudur.

    db=dosya.read()
    dosya.seek(0) # seek=byte ilerler
    db="b\n"+db
    dosya.write(db)


    # dosya oluşturuldu ve okutuldu.
    # dosyanın 0. byte'ına dönüldü ve tekrar çağırıldı.
    # yeni halini ve ham halini topla.
    # oluşturulan dosyayı yazdır.



# DOSYA ORTASINA VERİ EKLEME

    db=dosya.readlines()
    db.insert(2,"c\n")   # insert=ekleme komutu
    dosya.seek(0)
    dosya.writelines(db)   # satırlar arasına veri ekler
    


     