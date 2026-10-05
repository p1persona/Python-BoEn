
dosya=open("deneme.txt","w")

# write=hiç dosya oluşturulmadan önce, sıfırdan dosya oluşturmak kullanılır. hafızası yoktur.
dosya.write("merhaba p1")

# append=var olan dosyaya veri eklemek için kullanılır. "a"



# read=dosya içindeki verileri okumak için kullanılır.
b=dosya.read()
print(b)