#STRING FONKSİYONLAR VS.


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

print(cümle2.find("cimbom")) # çıktı 9 verdi çünkü 9. karakterde cimbombaşlıyor 0 la başlayıp sayar.


