#kendisine gönderilen kullanıcı adı ve şifreyi kontrol ederek
#sonucunda true ya da false gönderen fonksiyonun python kodu
#kullanıcıadı:admin, şifre:1234456 olmalı

def kontrol(kullanici,sifre):
    if kullanici=="admin" and sifre=="123456":
        return True
    else:
        return False
kullanici=input("kullanıcı adınızı giriniz:")
sifre=input("şifrenizi giriniz:")
sonuc=kontrol(kullanici,sifre)

if sonuc==True:
    print("başarılı giriş.")
else:
    print("lütfen tekrar deneyiniz.")