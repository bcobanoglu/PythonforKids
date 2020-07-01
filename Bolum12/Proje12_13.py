"""
Proje 12.13. 
Kenar sayısının diyalog kutuları ile girildiği çokgen çizimi yapan programı yeniden kodlayalım.
"""
#Çokgen çizimi
from turtle import *
#kenar sayısı giriliyor
N = int(numinput("Çokgen", "Kenar sayısı.:",6))
aci = 360/N #açı hesaplanıyor
pensize(2) #kalem ucu kalınlığı
#Çokgeni çiz
for i in range(N): 
    circle (50, aci, 1)
