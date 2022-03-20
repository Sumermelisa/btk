#kullanıcıdan bir sayı girmesini isteyen,
#sayı girmediğinde tekrar tekrar sayı girmesini isteyen program
#sayı girdiğinde sayının karesini yazdıran program

#while True:
#    try:
#        sayi=int(input("lütfen bir sayı giriniz."))
#        print("sayınızın karesi:",sayi*sayi)
#        print("teşekkürler.")
#        continue
#    except ValueError:
#        print("hatalı giriş.")

while True:
    try:
        sayi=int(input("lütfen bir sayı giriniz."))
        break
    except ValueError:
        print("hatalı giriş.")
print("sayınızın karesi:",sayi**2)
