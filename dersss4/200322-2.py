


    try:
        sayi1=int(input("bir sayı giriniz:"))
        sayi2=int(input("bir sayı giriniz:"))
        print("bölüm",sayi/sayi2)
    except ValueError:
        print("lütfen sayı giriniz.")
    except ZeroDivisionError:
        print("0'a bölme yapılamaz.")
    except SyntaxError:
        print("yazım hatası var.")
    except NameError:
        print("böyle bir değişken bulunamaktadır.")
    except:
        print("genel hata oluştu.")

print("program buradan çalışmaya devam eder...")
