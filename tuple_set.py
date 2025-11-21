# TUPLES-> Immutable yani sonradan değişemezler ama listeler sonradan değişebilir.

liste=["Emre","Kaan","Mehmet"]
liste[0]="Torreira"
print(liste)

tuples=("İlkbahar","Yaz","Sonbahar","Kış")
#tuples[0]="Ocak" bu satır çalışmaz çünkü tuple değişemez sonradan
print(tuples)

# Ama bazı fonksiyonları kullanabiliriz, listelerle ortak olarak.

print(liste.count("Emre"))
print(tuples.count("Yaz"))
print(liste.index("Mehmet"))
print(tuples.index("Kış"))


# SET (kümeler) normal matematikteki kümelerle aynı özellikte sayılır
sebzeler={"Ispanak", "Pırasa", "Lahana", "Patlıcan", "Patates","kiraz"}# kiraz sebze değil ama kesişimi göstermek için
meyveler={"elma","armut","kiraz","erik","kavun"} #ben buraya 2 tane kiraz yazsam da çıktıda 1 tane verir
print(meyveler)
print(sebzeler)
#elemanlar da sırasız şekilde verilir.
#print(type(meyveler))

# kümeler mutable'dir ekleme çıkarma yapılabilir.

#meyveler.add("çilek")
#print(meyveler)
#meyveler.remove("kiraz")
#print(meyveler)

#intersection (kesişim) union (birleşim) difference (fark)

print(meyveler.difference(sebzeler))
print(meyveler.intersection(sebzeler))
print(meyveler.union(sebzeler))


# örnek aşağıdaki listeyi ve set veri yapısını kullanarak tekrar eden elemanları silip aynı isimde ancak 
# içinde tekrar eden eleman olmayan bir liste haline dönüştürün!

number_list=[1,2,3,2,4,5,3,6,2,7,5,8]
new_set=set(number_list)
print(new_set)

number_list=list(new_set)

print(number_list)

#burada önemli 2 şey öğrendik set() bir veriyi kümeye dönüştürür.

#set([1, 2, 2, 3])    # {1, 2, 3}
#set((1, 2, 3))       # {1, 2, 3}
#set("emre")          # {'e', 'm', 'r'}
#set({"a": 1, "b": 2})# {'a', 'b'}
#set(range(4))        # {0,1,2,3}
# aynı şeyler liste için de geçerli



