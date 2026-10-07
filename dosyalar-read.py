
dosya=open("deneme.txt","r")

import codecs

with codecs.open("deneme.txt","r",encoding="utf-8") as dosya:     # encoding:türkçe karaktere çevirme
   

    a=dosya.readline(a)    # readline:metindeki ilk satırı verir. koordineli çalışır.

    a=dosya.readlines(a)   # veri array'leşir, indeks içerisine girer.

    say=1
    for i in a:
        print(say,":",i)
        say+=1

    a=dosya.readlines()
    print(a[2])



    
    a=dosya.read()
    print(a)