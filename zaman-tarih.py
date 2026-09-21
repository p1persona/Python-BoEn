

from datetime import datetime

a=datetime.now()
a=a.year
a=a.day
a=a.month
a=a.minute
print(a)

tam_tarih=datetime.strftime(a,"%c")
print(tam_tarih)


# %a hafta gününün kısaltması
# %A hafta gününün tam hali
# %b ayın kısaltması
# %B ayın tam hali
# %c tam tarih, saat ve zaman bilgisi
# %d sayı değerli bir karakter dizisi olarak gün
# %j belirli bir tarihin, yılın kaçıncı gününe denk geldiğini gösteren 1-366 arası bir sayı
# %n sayı değerli bir karakter dizisi olarak ay

import locale
locale.setlocale(locale.LC_ALL,"Turkish_Turkey.1254")  # türkçe'ye tanımlamak için