
class okul:
    def __init__(self,sube,ogretmen,bolum,mevcut):
        self.sube=sube
        self.ogretmen=ogretmen
        self.bolum=bolum
        self.mevcut=mevcut

    def bilgileri_goster(self):
        print("-"*45)
        print("SINIF BİLGİLERİ")
        print("Şube:{}\nÖğretmen:{}\nBölüm:{}\nMevcut:{}".format(self.sube,self.ogretmen,self.bolum,self.mevcut))
        print("-"*45)

    def ogrermen_adi(self):
        print("Öğretmen adı:",self.ogretmen)

birinci_sinif=okul("11/C","zehra uyar","yazılım","28")
birinci_sinif.bilgileri_goster()

ikinci_sinif=okul("9/B","rana uyar","öğretmenlik","46")
ikinci_sinif.bilgileri_goster()
ikinci_sinif.ogrermen_adi()