# dictionary(dict) ikili verileri tutmaya yarar örneğin öğrenci numarası öğrenci ismi gibi
# 100: Emre Yıldız 101: Kaan Apucu 102: Mehmet Turan Yardımcı

"""öğrenciler={100:"Emre Yıldız", 101: "Kaan Apucu", 102: "Mehmet Turan Yardımcı"}
print(type(öğrenciler))
print(öğrenciler)

#print(öğrenciler[103])
#eğer get ile değeri çağırırsam olmayan değeri none olarak döndürür ama diğer türlü direkt çağırırsam key error verir.

değer=print(öğrenciler.get(103))
print(type(değer))

print(öğrenciler.keys())
print(öğrenciler.values())

# dict'e değer ekleme


öğrenciler[103]="Tofiq Valiyev"
print(öğrenciler)

# değer çıkarma 2 farklı şekilde

öğrenciler.pop(101)
print(öğrenciler)

del öğrenciler[103]
print(öğrenciler)


termometre={100:25, 150:40, 200:[25,30,40]}
# 30'a erişmek için 
print(termometre[200][1])
(termometre[200][1])= 50
print(termometre[200][1])



kitaplar= [

    ("Şeker Portakalı",150),
    ("1984",200),
    ("Charlie'nin Çikolata Fabrikası",250),
    ("Harry Potter",300)
]

#for kitap in kitaplar:
 #   print(kitap[0], kitap[1])
toplam=0
for kitap_adı , kitap_sayfası in kitaplar:
    toplam+=kitap_sayfası

print(toplam)


öğrenciler={100: [75,80,90], 101: [40,60,75], 102: [100,90,100]}


# hem key hem de value değişkenlerini çağıracaksam items() kullanmalıyım yoksa biri gelir diğeri gelmez. 
for öğrenci_no, sınav_notları in öğrenciler.items():
    print(f"\nÖğrenci Numarası: {öğrenci_no}")
    print("-----------------------")
    for notu in sınav_notları:
        print(f"Öğrencinin sınav notu: {notu}")
"""


kitaplar=[

    ("Şeker Portakalı",180),
    ("Simyacı",184),
    ("1984",352),
    ("Hayvan Çiftliği",152)
]
kitaplar_170=[]
toplam=0
for kitap_adı,sayfa_sayısı in kitaplar:
    if sayfa_sayısı>170:
        print(kitap_adı,sayfa_sayısı)
        kitaplar_170.append((kitap_adı,sayfa_sayısı))

toplam=0

for kitap_adı,sayfa_sayısı in kitaplar_170:
    toplam+=sayfa_sayısı

print(f"Sayfa sayısı 170'ten fazla olan kitapların sayfaları toplamı {toplam}'dır")

    



