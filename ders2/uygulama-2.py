#kullanıcıdan 5 tane sayı isteyerek en büyük sayıyı listeye atayarak bulunuz


sayi1=input("1. sayıyı giriniz.")
sayi2=input("2. sayıyı giriniz.")
sayi3=input("3. sayıyı giriniz.")
sayi4=input("4. sayıyı giriniz.")
sayi5=input("5. sayıyı giriniz.")
sayilar=[]
print(sayilar)
sayilar.append(sayi1)
sayilar.append(sayi2)
sayilar.append(sayi3)
sayilar.append(sayi4)
sayilar.append(sayi5)
sayilar.sort(reverse=True) #veya sayilar.sort()/ print(sayilar[4]) > indeks 0 dan başlar
print("en büyük sayınız:",sayilar[0])

