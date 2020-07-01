"""
Proje 8.6. 
Bir string metni içerisindeki ‘,’ virgül karakterlerinden ayrıştırarak listeye dönüştüren programı kodlayalım.

"""
metin = "*,**,***,****"
liste = metin.split(",")
for x in liste:
    print (x)
