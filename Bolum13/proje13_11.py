"""Çocuklar için Python, Bülent Çobanoğlu
Proje13_11: Çokgen Çizimi
"""
from turtle import *
N= int(input("Kenar sayısı.: "))
aci = 360/N #Açı hesaplandı
pensize(2) #Kalem kalınlığı seçildi
# N-gen çizimi döngü içerisinde yapıldı
for i in range(N):
    forward(50) #50 birim ileri git
    left(aci) #Açı derecesi kadar sola dön