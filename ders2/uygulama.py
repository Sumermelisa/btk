#kullanıcıdan ad soyad telefon alarak bilgiler adlı listeye atayınız

bilgiler=[] #boş liste tanımla
isim=input("adınız?")
soyad=input("soyadınız?")
tel=input("telefon numaranız?") #kullanıcıdan bilgileri al>input kullan
gun=input("doğum tarihiniz?")
yas=input("yaşınız?")
print(bilgiler) #boş listenin elemanlarını kullanıcıdan al
bilgiler.append(isim) #append ile listeyi aldığın bilgilerle doldur
bilgiler.append(soyad)
bilgiler.append(tel)
bilgiler.append(gun)
bilgiler.append(yas)
print(bilgiler) #doldurulan yeni listeyi yaz

