"""
Proje 12.7. 
Şekildeki gibi kahverengi üçgen çatılı ve mavi kareli bir ev çizen programı kodlayalım.
"""
from turtle import *
#kare çizme fonksiyonu
def kareCiz(boyut):
    for x in range(1, 5):
        forward(boyut)
        right(90)
#üçgen çizme fonksiyonu
def ucgenCiz(boyut):
   for x in range(1, 4):
         forward(boyut)
         left(120)
         
#ana program
pensize(3) #çizgi kalınlığı
begin_fill() #üçgeni boya
fillcolor("brown") #içi kahve
ucgenCiz(100)
end_fill() #boyamayı kaldır

begin_fill() #kareyi boya
fillcolor("blue") #içi mavi
kareCiz(100)
end_fill() #boyamayı kaldır
