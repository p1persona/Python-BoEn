
# GLOBAL VE YEREL DEĞİŞKENLER

def fonksiyon():
    a=5
    print(a)

fonksiyon()



a=10
def fonksiyon():
    print(a)

fonksiyon()



#DIŞARDAKİ DEĞİŞKENİ İÇERDE KULLANABİLİRSİN AMA İÇERDEKİ DEĞİŞKENİ DIŞARDA KULLANAMAZSIN.


a=10

def fonksiyon():
    global a
    a=25
    print(a)

fonksiyon()
