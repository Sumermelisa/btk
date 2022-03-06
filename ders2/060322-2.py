liste=[] #boş liste tanımlar
liste=["elma","armut",20] #artık listenin elemanları değişti
sayilar=[15,3,7,9,505,222]
isimler=["şukufe","denizcan","pelinsu","hatice"]
gunler=["pazartesi","salı","çarşamba"] #ctrl+d çoğaltır, ctrl+y satırı siler
print(gunler) #indeks 0 dan başlar
print("0. indeksdeki eleman:",gunler[0])
print(gunler[1])
print(gunler[2])
gunler.append("perşembe")#append yeni eleman ekler
print(gunler)
print("eleman sayısı:",len(gunler)) #len: listenin eleman sayısını verir
gunler.pop() #hiçbir şey yazılmazsa listenin son elemanını çıkarır
print(gunler)
gunler.pop(0) #0. indeksdeki elemanı siler
print(gunler)
print(sayilar)
sayilar.sort() #default küçükten büyüğe sıralar
print(sayilar)
sayilar.sort(reverse=True) #büyükten küçüğe doğru sıralar
print(sayilar)
isimler.sort() #default alfabetik sıralama
print(isimler)

