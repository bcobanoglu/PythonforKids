"""
Çocuklar için Python,
Proje 12.2. 
Ekrana farklı boyutlarda iç içe 3 adet kare çizen programı kodlayalım.

"""
from turtle import *
#kare çizme fonksiyonu
def kareCiz(mesafe):
    for x in range(1, 5):
        forward(mesafe)
        left(90)

#Ana program
#Kaplumbağa simgesi yok
shape('blank')
#kalem kalınlığı 2 birim
pensize(2) 
#iç içe 3 kare çiz
kareCiz(50) 
kareCiz(100)
kareCiz(150)
