tuttugumsayi=222

while True:
    sayi=int(input("tahmininiz:"))
    if sayi<tuttugumsayi:
        print("bilemediniz,sayıyı büyütün.")
    elif sayi>tuttugumsayi:
        print("bilemediniz,sayınızı küçültün.")
    else:
        print("tebrikler.. doğru tahmin..")
        break