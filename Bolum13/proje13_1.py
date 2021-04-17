"""Çocuklar için Python, Bülent Çobanoğlu
Proje13_1: Kare Çizimi: Sıra Sende Etkinliği-1
"""
from turtle import *
#kare çizme fonksiyonu
#döngü ile
def kareCiz():
    for i in range(4):
        forward(100)
        left(90)
#Ana program
kareCiz()
