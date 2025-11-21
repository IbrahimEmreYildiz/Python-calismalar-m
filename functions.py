# fonksiyonlar belirli bir görevi yerine getiren kod bloklarıdır. Bir kere çağırıldıktan sonra tekrar tekrar
# çağrılabilir. Kodun daha düzenli daha okunulabilir olmasını sağlar.


# fonksiyon tanımlama def= definition
 
def fonksiyon_adı():
    işlem bloğu


#basit fonksiyon tanımı
def ekrana_yazdırma():
    print("Merhaba!")
    print("Hoşgeldiniz..")

ekrana_yazdırma()

# parametreli fonksiyon

def selamla(isim): 
    print("Merhaba Hoşgeldin", isim)
    isim = "Mehmet"
    print("Merhaba Hoşgeldin", isim)

isim = "Kaan"
selamla(isim)
selamla(isim)


#return içeren fonksiyonlar - return yanına yazdığımız şeyi döndürür.

def carp(x, y):
    print(" Çarpım işlemi yapılıyor..")
    return x*y # Burada return x ve y ye atanan parametrelerdeki değerlerin çarpımını döndürür
# ama print kullanmazsanız o dönen değeri yazdırmaz çünkü fonksiyonumuzd print kullanmadık.
print("Çarpım:", carp(3, 5))

# Global değişken o fonksiyonun dışındaki değişken local değişken ise fonksiyonun içinde tanımlanan değişkendir.
# Ben fonksiyonun içine global veri tipini kullanırsam bu fonksiyonun içindeki değişkeni fonksiyonun dışındaki 
# ile aynı yapar.


def örnek():
    x=5 # local x
    print("local x:",x)


def örnek2():
    global x # burada global veri tipi kullandığım için global x yani x= 10 olur.
    x=x*10
    print(" global x:", x)

def örnek3(): # fonksiyonun içinde x tanımlamadığım için dışarıda x aradı ve onu kullandı.
    y=2
    toplam= x+y
    print("Toplam:",x+y)


x=10 # global x
print("Global x:",x)
örnek()
örnek2()
print(x)
örnek3()

# fonksiyonun içinde fonksiyon tanımlayabilirim

def örnek4():
    selamla()
    x=5
    print("Local x:",x)

def selamla():
    print("Selamsss")

örnek4()

#eğer selamla fonksiyonunu örnek4 ü yazdırdığım yerin altına koysaydım hata alırdım
#Çünkü örnek 4 e gelene kadar fonksiyonu tanımlamamış olurdum.
"""
"""
# Bölme ve çıkarma işlemi yapan fonksiyonlar yaz bölünen ve bölen parametre olsun bölen 0 olursa uyarı ver.
#sonuçları döndür.


def bölme(x,y):
    if y==0:
        print("Bir sayının 0 ile bölümü tanımsızdır")
        return "Hatalı İşlem"
    else:
        return x//y#print("Sonuç:", x//y)
   #eğer herhangi bir şey return etmezse none yazar çıktıda.


def çıkarma(a,b):
    return a-b


print(bölme(12,3))
print(bölme(12,0))
print(çıkarma(12,3))



# Default yani fonksiyonda varsayılan parametre

def selamla(isim = "Misafir"):
    print("Merhaba", isim)


selamla("Ahmet")
selamla() #Normalde bu hata verirdi ama fonksiyonu tanımlarken default değer girdiğimiz için parametre olarak onu alır.


# Sayısı belli olmayan parametreler

def toplama(*args):
    return sum(args) # bu bir tupledir (1,2,4,6) gibi sadece sayısı belli olmayan bir tuple

print("toplam: ", toplama(1,2,3,4))





# fonksiyon örnek çözümü 

#ağırlıklı ortalama bulma 3 tane sınav notu girilecek (mt1,mt2,f) sırasıyla %20,%35,%45 olarak etkili
#ortalamayı ekrana yazdırın. ortalama 50 den azsa veya final 20 den küçükse midterm 
#ne olursa olsun büte kaldınız yazdır.


def ağırlıklı_ortalama(mt1,mt2,f):
    ort= (mt1*20/100)+(mt2*35/100)+(f*45/100)
    if ort<50 or f<20:
        print("Ortalamanız:",ort)
        print("Büt sınavına girmelisiniz. Gerekli şartları sağlayamadınız.")
       
    else:
        print("Tebrikler dersi geçtiniz!")
        print("Ortalamanız:",ort)


ağırlıklı_ortalama(70,64,19)


#**kwargs kullanımı : Dictionary olarak kullanılabilir args ile aynı sadece kw var keyword demek buradan
# dict olduğunu anlayabiliriz.

def kisi_bilgileri(**kwargs):
    print("Ad:", kwargs["ad"])
    


kisi_bilgileri(ad="Emre",Soyad="Yıldız", Yaş="24")

#recursive(kendini çağıran fonksiyonlar)


def faktoriyel(n):
    if n==1:
        return 1
    else:
        return n*faktoriyel(n-1)
    
print(faktoriyel(5))

#lambda fonksiyonlar (tek satırlık fonksiyonlar)

topla=lambda x,y: x+y # tek satırlık

print((lambda x,y:x-y)(5,3)) # anonim fonksiyon bunu başka satırda kullanamazsın 
#tanımlamadığın için isim olarak.

print(topla(3,5))



#fonksiyonu parametre olarak kullanmak

def ucle_carp(function, sayi):
    return function(sayi)*2

def kup_al(a):
    return a**3

print(ucle_carp(kup_al,4))


#Listenin içindeki sayıları filtreleyip çift olanları tanımlayan yeni bir liste oluştur ve
# list comphrehension kullan

sayilar=[1,2,3,4,5,6,7,8,9,10]


def cift_sayilar(sayilar):
   return [sayi for sayi in sayilar if sayi%2==0]

sonuc=cift_sayilar(sayilar)

print("Çift sayılar=",sonuc)


kelimeler=["karpuz", "elma", "kardan adam", "kayak", "kar fırtınası", "güneşli hava"]


def kar_filtrele(kelimeler):
    kar_filtreleme = []
    for kelime in kelimeler:
        if "kar" in kelime:
            kar_filtreleme.append(kelime)
    return kar_filtreleme
    
    return [kelime for kelime in kelimeler if "kar" in kelime]

print(kar_filtrele(kelimeler))




# fibonacci fonksiyonu yaz kullanıcıdan bir sayı iste en büyük sayı o sayıya eşit veya küçük olana kadar devam etsin


def fibonacci():
    while True:
        n= int(input("Lütfen bir sayı gir(2'den büyük olması gerekli): "))
        if n<=2:
            print("Sayı 2'den büyük olmalı!\n")
        else:
            break
        
    fib_serisi=[]
    a=0
    b=1
    while a<=n:
        fib_serisi.append(a)
        temp=a+b
        a=b
        b=temp

    print("Fibonacci Serisi= ",fib_serisi)
    


fibonacci()

