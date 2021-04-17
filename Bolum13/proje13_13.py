#Çokgen çizimi
from turtle import *
#kenar sayısı giriliyor
N = int(textinput("Çokgen", "Kenar sayısı.:"))
aci = 360/N #açı hesaplanıyor
pensize(2) #kalem ucu kalınlığı
title(str(N) + "-GEN")
#Çokgeni çiz
for i in range(N):
    circle (50, aci, 1)