import random
while True:
    seviye=input("lütfen bir seviye seçiniz:kolay/orta/zor ")


    if seviye=="kolay":
        uret=random.randint(1,10)
        break
    elif seviye=="orta":
        uret=random.randint(1,50)
        break
    elif seviye=="zor":
        uret=random.randint(1,100)
        break
    else:
        print("lütfen geçerli bir seviye giriniz.")

while True:
    tahmin=int(input("lütfen tahmininizi giriniz:"))

    if tahmin<uret:
        print("sayınızı büyütün.")
    elif tahmin>uret:
        print("sayınızı küçültün.")
    else:
        print("tebrikler,doğru tahmin!")
        break