
# MODÜLLER

from ... import ...





# RANDOM

#rastgale sayılar üretir
import random 

print(dir(random))

a=dir(random)
print(a)


print(random.random())

a=random.random()
print(a)
print(round(a*10,2))



#UNIFPORM

#belirli aralık arasında PARAMETRE ALARAK rastgale sayılar üretir.
a=random.uniform(1.3,5.6)
print(a)



# RANDINT 

#başlangıç-bitiş arasında sayı üretir.
a=random.randint(67,89)
print(a)



# LIST

#liste içinden veri seçer.
list=["a","b","c"]
a=random.choice(list)



#SHUFFLE

#liste özelliği taşıyan verileri karıştırır.
a=random.shuffle(list)
print(list)



#SAMPLE

#belirlenen sayı kadar numune seçer.
print(random.sample(list,1))