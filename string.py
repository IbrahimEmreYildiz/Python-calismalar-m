#STRING FONKSİYONLAR VS.

"""
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
"""
"""
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
"""
"""
string.isalpha() -> Tüm karakterler harf ise True, değilse False.  
string.isdigit() -> Tüm karakterler sayı ise True, değilse False.  
string.isalnum() -> Harf veya rakam (alfanümerik) ise True, değilse False.  
string.islower() -> Tüm harfler küçük ise True, değilse False.  
string.isupper() -> Tüm harfler büyük ise True, değilse False.
"""
""""
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
"""

"""

# python çoklu atama (unpacking ya da destructring)

metin="104, Ali, Çalışkan, 89"

numara, ad, soyad, ortalama= [parca.strip() for parca in metin.split(",")] #Burada değişkenler tek tek parca'ya atanır
# Örneğin parca=104 olur boşluk varsa temizler sonra Ali parcaya atanır ve boşluklar temizlenir..

print("Numara:", numara, "Ad:", ad, "Soyad:", soyad, "Ortalama:", ortalama)
"""

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
