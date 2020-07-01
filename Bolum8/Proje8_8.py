"""
Proje 8.8. 
Şifre/password sorgulaması yapan bir programı kodlayalım.

"""

sayac=0
while True:
    sifre=input("Password.:")
    if sifre=="elma":
        print ("Şifre doğru")
        break
    sayac+=1
    if sayac>=3:
        print ("Hakkınız bitti")
        break
