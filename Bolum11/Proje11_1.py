"""Çocuklar için Python
Proje 11.1. 
Yarıçap (r) uzunluğu klavyeden girilen bir dairenin alanını ve çevresini hesaplayan programı kodlayalım. 

"""
import math #pi sayısı için gerekli

r = int(input("Yarıçapı gir.:"))
Alan = math.pi * pow(r,2)
Cevre = 2 * math.pi * r
print ("Dairenin Alanı=", Alan)
print ("Dairenin Çevresi=", Cevre)
