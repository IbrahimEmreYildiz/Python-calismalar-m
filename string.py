#STRING FONKSİYONLAR VS.
import random

metin="Emre yıldız"
# Karakter sayısı
print(len(metin))
print(len("Emre"))

# upper() lower() full büyük ve full küçük

print(metin.upper())
print(metin.lower())

#capitalize() title() Sadece ilk kelimenin ilk harfi büyük - Her kelimenin ilk harfi büyük

print(metin.capitalize())
print(metin.title())

# strip() - lstrip() - rstrip() tüm boşlukları siler - soldaki boşlukları siler - sağdaki boşlukları siler
metin1="   Merhaba Python     "
print(metin1.strip(),".")
print(metin1.lstrip(),".")
print(metin1.rstrip(),".")

# replace() belli bir kelimeyi diğeriyle değiştirir

metin2= "Python öğreniyorum Python çok keyifli. Python kolpa"

yeni_metin= metin2.replace("Python", "C++",2) # 2 sadece ilk 2 tanesini değiştir demek
print(yeni_metin)


# split() kelimeleri listeye çevirir.

cümle= "Galatasaray çok iyi bir takım."
print(cümle.split())


# join() bir liste verdiğimizde listeyi düz stringe çevirir

list=["Solo","il","Gala"]
cümle1= " ".join(list) #aralarına boşluk bırak diyebilmek için ekledik tırnak işaretini
print(cümle1)


# find() cümlede aradığımız kelimenin kaçıncı karakterde başladığını söyler

cümle2= "En büyük cimbom"

print(cümle2.find("büyük")) # çıktı 9 verdi çünkü 9. karakterde cimbombaşlıyor 0 la başlayıp sayar.


#index kelimenin başladığı karakterin indexini verir. find() ile farkı find bulamazsa -1 döndürür index() ise
# ValueError verir.

print(cümle2.index("büyük"))

# count() Aradığımız kelime veya cümlenin kaç kere geçtiğini bulur. 
# Püf noktası boşluklara vs. dikkat etmem lazım aradığım kelimenin.

cümle3=" Python diğer dillere göre çok kolay bir dil. Python 'u seviyorum."

sayaç= cümle3.count(" Python ")
print(sayaç)

# Birkaç basit fonksiyon

string.isalpha() -> Tüm karakterler harf ise True, değilse False.  
string.isdigit() -> Tüm karakterler sayı ise True, değilse False.  
string.isalnum() -> Harf veya rakam (alfanümerik) ise True, değilse False.  
string.islower() -> Tüm harfler küçük ise True, değilse False.  
string.isupper() -> Tüm harfler büyük ise True, değilse False.

a = "Merhaba"
b = "Merhaba123"
print(a.isalpha())   # True  → sadece harfler var
print(b.isalpha())   # False → içinde rakam da var

x = "12345"
y = "12a45"
print(x.isdigit())   # True  → tamamen rakamlardan oluşuyor
print(y.isdigit())   # False → içinde harf var

t1 = "Python3"
t2 = "Python 3"
print(t1.isalnum())  # True  → sadece harf ve rakam var
print(t2.isalnum())  # False → arada boşluk var, o yüzden alfanümerik değil

s1 = "python"
s2 = "Python"
print(s1.islower())  # True  → tüm harfler küçük
print(s2.islower())  # False → ilk harf büyük

k1 = "HELLO"
k2 = "Hello"
print(k1.isupper())  # True  → tüm harfler büyük
print(k2.isupper())  # False → bir harf küçük



# python çoklu atama (unpacking ya da destructring)

metin="104, Ali, Çalışkan, 89"

numara, ad, soyad, ortalama= [parca.strip() for parca in metin.split(",")] #Burada değişkenler tek tek parca'ya atanır
# Örneğin parca=104 olur boşluk varsa temizler sonra Ali parcaya atanır ve boşluklar temizlenir..

print("Numara:", numara, "Ad:", ad, "Soyad:", soyad, "Ortalama:", ortalama)


# burada püf nokta şu reverse() yeni bir dizi oluşturmaz mevcut diziyi değiştirir
# ve join ise sadece string içeren listelere uygulanır 
# ve önden listenin üyeleri arasına ne koyacağını belirtmen lazım.

veri=input("Lütfen bir cümle giriniz: ")

büyük= veri.upper()
print(büyük)

ayrık= büyük.split(" ")
print(ayrık)
ayrık.reverse()
son=" ".join(ayrık)

print(son)


# Bir stringi değiştirmek python'da imkansız sadece yeni bir string oluşturarak yapabiliriz

metin= "Python çalışıyorum"

metin= "Z" + metin[1:]

# Kullanıcıdan bir kelime al kelimeyi tersten yazdır ama 2 türlü bir for döngüsü bir de slicing
# Örnek Python-nohtyP

kelime=input("Kelime giriniz: ")

print(kelime[::-1]) # slicing'de -1 tersten gelerek 1er 1er yaz demek

# for ile çözüm
ters_kelime=""

for harf in kelime:
    ters_kelime= harf + ters_kelime
print(ters_kelime)

# Bir cümledeki aradığımız harf sayısı ve onun ilk bulunduğu index

sentence=input("Lütfen bir cümle giriniz: ")

while True:
    character=input("Lütfen bir harf giriniz:")
    if len(character) != 1:
        print("Sadece 1 harf giriniz!")
    else:
        break

index = sentence.find(character)
tane = sentence.count(character)
if index==-1:
    print("Aradığınız harf cümlede yok.")

else:

    print(f"Aradığınız harf cümlede {tane} kere var ve bulunduğu ilk index {index}. indextir.")

# içinde aradığımız harf bulunan kelime sayısı


cümle=input("Lütfen cümle gir: ")
harf=input("Lütfen harf gir: ")

kelimeler= cümle.split()
sayac=0
for kelime in kelimeler:
    if harf in kelime.lower():
        sayac+=1

print(f"İçinde aradığımız harf bulunan kelime sayısı {sayac}'tır.")

"""
Aşağıdaki adımları izleyerek bir Python programı yazınız:

I. Adım) 1 ile 35 arasında (1 ve 35 dahil) rastgele üretilen tam sayılardan oluşan bir liste oluşturun. 
Bu liste, 1 haftanın (7 günün) her bir günü için ölçülen ortalama sıcaklık değerlerini temsil etsin.

II. Adım) Bu listeyi ekrana yazdırın.

III. Adım) Bu 7 günün (yani haftanın) ortalama sıcaklığını hesaplayıp ekrana yazdırın.
"""


sicaklik_ortalaması=[]

for sayi in range(7):
    sayi= random.randint(1,35)
    sicaklik_ortalaması.append(sayi)

print("Haftanın sıcaklık değerli şu şekildedir:",sicaklik_ortalaması)

toplam=0

for sicaklik in sicaklik_ortalaması:
    toplam +=sicaklik

ortalama=toplam/7
ortalama = round(ortalama,2)
print(f"Sıcaklık ortalaması {ortalama}'dır.")