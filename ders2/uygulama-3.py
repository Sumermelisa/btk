#kullanıcıdan harf girmesini isteyiniz e girerse erkek k girerse kadın yazdırınız ekrana

cinsiyet=input("cinsiyetiniz?(k/e)") #int sadece ssayılarda, diğerleri str
if  cinsiyet== "k" or cinsiyet=="K" : #normalde böyle yapılmaz
    print("kadın")# or veya, and ve
elif cinsiyet== "e" or cinsiyet=="E": #ikinci veya daha fazla şartlarda elif (else/if) kullanılır
    print("erkek")
else:
    print("lütfen geçerli bir harf giriniz.")
print("teşekkürler")