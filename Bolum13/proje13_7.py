"""Çocuklar için Python, Bülent Çobanoğlu
Proje13_7: Ev çizimi
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
colormode(255)
color(0,0,255) #içi mavi: eşdeğeri: color("blue") 
kareCiz(100)
end_fill() #boyamayı kaldır