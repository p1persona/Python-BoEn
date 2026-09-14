
# SPLIT METODU

deneme="clary,specter,zehra,uyar"
print(deneme)

deneme=deneme.split()
print(deneme)




deneme="clary specter zehra uyar"
print(deneme)

deneme=deneme.split()
print(deneme[1])




tarih="16/08/2000"
tarih=tarih.split(("/"))
print(tarih)



veri_al=input("parçalanacak keliemeler:")
for i in veri_al:
    print(i)



for i in veri_al.split():
    print(i[2],end="")