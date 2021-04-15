#Çocuklar için Python, Bülent Çobanoğlu
# -*- coding: utf-8 -*-
"""Proje5_8.py : TCDD İndirimli Bilet Fiyatlandırması
Yaş 			İndirim Oranı
0 - 6 arası 	Ücretsiz
7 – 12 arası 	%50
13 – 26 arası 	%20
27 - 59 		%0	
60 – 64 		%20
65 ve üzeri 	%50
Girilen yaş değerine göre indirimli bilet fiyatını gösteren programı kodlayalım.
""" 
Fiyat = 100
yas = int (input('Yaşınız.:'))
print ("Normal Bilet Fiyatı.:", Fiyat)
if yas>0 and yas<=6:
	iFyt = 0 #ücretsiz
elif yas>=7 and yas<=12:
	iFyt=Fiyat/2 # %50 indirim
elif yas>=13 and yas<=26:
	iFyt=Fiyat- Fiyat*0.20
elif yas>=27 and yas<=59:
	iFyt=Fiyat #indirim yok
elif yas>=60 and yas<=64:
	iFyt=Fiyat- Fiyat*0.20
elif yas>=65:
	iFyt=Fiyat/2 #%50 indirim
print ("İndirimli Bilet Fiyatı.:", iFyt)
