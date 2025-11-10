#listeden en büyük elemanı bulma, eleman sayısını vs. bulma
isimler=["Ali","Ece","Kaan","Mete","Batu","Veli","Ayşe"]
numaralar=[145,178,164,175,185,180,134]

öğrenci_adı=""
max_num=numaralar[0]
min_num=numaralar[0]

for i in range(len(numaralar)):
    if numaralar[i]>max_num:
        max_num=numaralar[i]
        öğrenci_adı=isimler[i]

print (f"En büyük numaralı öğrenci {max_num} numarasıyla {öğrenci_adı} olmuştur.")

for i in range(len(numaralar)):
    if numaralar[i]<min_num:
        min_num=numaralar[i]
        öğrenci_adı=isimler[i]
print(f"En düşük numaralı öğrenci {min_num} numarasıyla {öğrenci_adı} olmuştur.")

#python'un kendi fonksiyonları
max_numara=max(numaralar)
print(max_numara)
max_index= numaralar.index(max_numara)
print (isimler[max_index])
