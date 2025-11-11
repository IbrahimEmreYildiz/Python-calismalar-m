# WHILE

#While'da sayılar otomatik artmaz ama "for"da artar böyle bir fark var.
#Ne zaman biteceği belli değilse genelde while kullanılır.

#kullanıcı bir sayı girecek ve ben sürekli onun karesini yazdıracam.Sayı aralığı aldım 
# Ve önce küçük sayıyı girebilmesi için zorladım. Girdiği aralıktaki pozitif tam sayıların karesini
# liste şeklinde yazdırdım.


print("Şimdi sayı aralığı gireceksiniz. Lütfen önce küçük sayıyı giriniz..")
while True:
    sayi = int(input("Küçük sayıyı giriniz: "))
    sayi1 = int(input("Büyük sayıyı giriniz: "))
    if sayi < sayi1:
        break
    else:
        print("İlk sayı ikinci sayıdan küçük olmalı, lütfen tekrar giriniz.")


squares=[]

while sayi>=0 and sayi1>=0:
    squares.append(sayi**2)
    sayi+=1
    if sayi==sayi1:
        break
print("Kareler listesi:", squares)



# Hesap makinesi menülü ve bölmede bölen 0 olamaz şekilde ayarlandı.

print("1. Toplama \n2.Çıkarma \n3.Çarpma\n4.Bölme\n5.Çıkış")

secim= int(input("Lütfen bir sayı giriniz: "))
if secim==5:
    print("Programdan çıkış yapılıyor...") 
elif secim>5 or secim<1:
    print("Geçerli bir sayı girmediniz! Program Sonlandırılıyor..")
else:
    sayi1=int(input("Lütfen işlem yapacağınız sayıyı giriniz..: "))
    if secim==4: 
        while True:
            sayi2=int(input("Lütfen 0'dan farklı bir sayı giriniz.. "))
            if sayi2==0:
                print("2. sayı 0 olmaz lütfen farklı bir değer giriniz!")
            else:
                print("İşlem sonucunuz: ", sayi1//sayi2)
                break
    else :
        sayi2=int(input("Lütfen işlem yapacağınız diğer sayıyı giriniz..: "))

    if secim==1:
        print("İşlem sonucunuz: ", sayi1+sayi2)

    elif secim==2:
        print("İşlem sonucunuz: ", sayi1-sayi2)

    elif secim==3:
        print("İşlem sonucunuz: ", sayi1*sayi2)  
    
    
       


     
