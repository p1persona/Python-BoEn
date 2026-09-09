
# INPUT

kullanici_adi = input("lütfen adınızı yazın:")
kullanici_ps = int(input("lütfen şifrenizi yazın:"))



# alıştırma

vize_puani = int(input("lütfen vize notunuzu giriniz:"))
final_puani = int(input("lütfen final puanınızı giriniz:"))

ortalama_hesapla = (vize_puani+final_puani) / 2

print("*"*30)
print(f"vize puanınız:{vize_puani}\nfinal puanınız:{final_puani}\nortalamanız:{int(ortalama_hesapla)}")