

giris =("""hesap makinesi
1-topla
2-çıkar
3-çarp
4-böl
5-çık""")

print(giris)

while True:
    islem=int(input("işleminizi giriniz:"))

    if islem==5:
        print("çıkış yaptınız.")
        break


    elif islem==1:
        sayi1= int(input("ilk sayıyı giriniz."))
        sayi2= int(input("ikinci sayıyı giriniz."))
        print("sonucunuz", sayi1 + sayi2)
    elif islem==2:
        sayi1 = int(input("ilk sayıyı giriniz."))
        sayi2 = int(input("ikinci sayıyı giriniz."))
        print("sonucunuz",sayi1-sayi2)
    elif islem==3:
        sayi1 = int(input("ilk sayıyı giriniz."))
        sayi2 = int(input("ikinci sayıyı giriniz."))
        print("sonucunuz",sayi1*sayi2)
    elif islem==4:
        sayi1 = int(input("ilk sayıyı giriniz."))
        sayi2 = int(input("ikinci sayıyı giriniz."))
        print(sayi1/sayi2)


    else:
        print("lütfen geçerli bir işlem seçiniz.")
