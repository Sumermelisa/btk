#kullanıcıya sürekli isim sorulsun q ya basınca çıksın

giris=""" isminizi giriniz.
(çıkış için q ya basınız.)
"""
print(giris)

#while True:
#    isim=input("lütfen isminizi giriniz.")

#    if isim=="q":
#        print("çıkış yapıldı.")
#        break

isim=""
while isim!="q": # != eşit değil. if not. olumsuzu
    isim=input("isminizi giriniz.")
    if isim=="q":
        print("çıkış yapıldı.")
