"""Çocuklar için Python, Bülent Çobanoğlu
Proje13_9: #daire çizimi
"""
from turtle import *
pensize(3) #kalın uç
#kalem: siyah, iç dolgu: kırmızı renkli
color("black", "red")
begin_fill() #boyama başla
circle(50) #yarıçapı:50
end_fill() #boyamayı bitir