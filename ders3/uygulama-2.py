#kullanıcı adı ve şifre alınız.. kullanıcı adı olarak "admin" şifre olarak 123456
#girilince "sisteme başarı ile giriş yapıldı" yazsın..
#yanlış girildilçe "kullanıcı adı veya şifre hatalı" yazıp tekrar kullanıcı adı ve şifre sorulsun

giris= """lütfen kullanıcı adı ve şifrenizi giriniz"""
print(giris)
while True:
    isim=input("kullanıcı adı?")
    sifre=input("şifre?")


    if isim=="admin" and sifre=="123456":
        print("başarılı giriş")
        break

    else:
        print("kullanıcı adı veya şifre yanlış",
                "lütfen tekrar deneyiniz.")
