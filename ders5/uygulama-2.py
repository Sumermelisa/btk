#dikdörtgenin alanını ve çevresini hesaplayan
#iki ayrı fonk yazınız
#kullanıcıdan aldığınız verilere göre ekrana yazdırınız

def alan(a,b):
    return a*b
def cevre(a,b):
    return (a+b)*2

sayi1=int(input("lütfen birinci sayıyı giriniz:"))
sayi2=int(input("lütfen ikinci sayıyı giriniz:"))
sonuc1=alan(sayi1,sayi2)
sonuc2=cevre(sayi1,sayi2)

print("dikdörtgeninizin alanı:",sonuc1)
print("dikdörtgeninizin çevresi:",sonuc2)