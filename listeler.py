
# LISTELER
listeler = ["zehra","uyar",200]

print(listeler)
print(len(listeler))
print(listeler[0])


# en sona ekleme
listeler.append("clary")
print(listeler)

# istenilen kısma ekleme
listeler[2] = "kamer"
print(listeler)

# istenilen kısma kadar alma
print(listeler[:2])

# veri değiştirme
listeler[:2] = ["p1","person"]
print(listeler)

# belirli aralığı alma
print(listeler[0:3])

# belirli kısmı silme
listeler[0:3] = []
print(listeler)