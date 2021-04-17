'''Çocuklar için Python, Bülent Çobanoğlu
Proje 12.1. Dairenin Alanını ve Çevresini Hesaplama:
Yarıçap (r) uzunluğu klavyeden girilen bir dairenin alanını ve çevresini hesaplayan
programı kodlayalım'''

import math #pi sayısı için gerekli
r = int(input('Yarıçapı gir.:'))
Alan = math.pi * pow(r,2)
Cevre = 2 * math.pi * r
print ("Dairenin Alanı=", Alan)
print ("Dairenin Çevresi=", Cevre)