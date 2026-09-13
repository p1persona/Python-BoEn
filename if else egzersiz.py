vize = int(input("vize notunuzu giriniz:"))
final = int(input("final notunuzu giriniz:"))

ortalama = (final+vize)/2

if ortalama>=85:
    print("AA aldınız:",ortalama)

elif ortalama>=65:
    print("BB aldınız:",ortalama)

elif ortalama>=50:
    print("CC aldınız:",ortalama)

else:
    print("ders tekrarı alın:",ortalama)