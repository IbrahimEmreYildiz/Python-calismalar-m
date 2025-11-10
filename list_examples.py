import random
# from random import shuffle  diyerek sadece shuffle kullanablirm
#List Compherension
"""
sayilar=[1,2,3,4,5,6,7,8,9,10]
kelimeler=["python","computer","vision","learning"]
buyuk_harfler=[]
ciftler=[]
ciftlerin_karesi=[]

for x in sayilar:
    if x%2==0:
        ciftler.append(x)
print (ciftler)

ciftlerin_karesi=[x**2 for x in sayilar if x%2==0]
print(ciftlerin_karesi)


buyuk_harfler=[kelime.upper() for kelime in kelimeler]
print(buyuk_harfler)
"""
# BREAK and CONTINUE
"""
for x in range(1,11):
    if x==5:
        print("Döngü break komutuyla durduruldu!")
        break
    print(x)

for sayi in range(1,9):
    if sayi == 4:
        continue
    print(sayi)
   
# RANDOM MODÜLÜ
#zar atmış gibi oluyor
print(random.randint(1,6))
sayi=random.randint(1,6)
print (sayi)
"""
#shuffle
list=[1,2,3,4,5,6,7,8]
print("Karıştırılmadan önce: ", list)
print("Karıştırılıyor...")
random.shuffle(list)
print("Karıştırıldıktan sonra: ", list)