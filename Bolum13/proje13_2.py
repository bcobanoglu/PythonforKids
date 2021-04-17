"""Çocuklar için Python, Bülent Çobanoğlu
Proje13_2: İçiçe Kare Çizimi
"""
from turtle import *
#kare çizme fonksiyonu
def kareCiz(mesafe):
    for x in range(1, 5):
        forward(mesafe)
        left(90)
#Ana program
shape('blank')#Kaplumbağa simgesi yok
pensize(2)#kalem kalınlığı 2 birim
#iç içe 3 kare çiz
kareCiz(50)
kareCiz(100)
kareCiz(150)