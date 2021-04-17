"""Çocuklar için Python, Bülent Çobanoğlu
Proje13_6: Kare çizimi
"""
from turtle import *
#kare çizen fonksiyon
def kareCiz():
    for x in range(4):
        forward(100)
        left(90)
#çizgi rengi kırmızı, içi sarı
color ("red", "yellow")
#şeklin içini de boya
begin_fill()
kareCiz()
end_fill()