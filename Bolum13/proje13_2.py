"""Bülent Çobanoğlu,
Proje 13.2. 
Grafik ekranına klavyedeki yön tuşlarını kullanarak çizim yapan programı kodlayalım.
"""
from turtle import *
shape('turtle') #kaplumbağa
pensize(3)#kalem kalınlığı
setup(300,300)#Çizim ekran boyutu
#yön tuşları için fonksiyonlar
def solaDon():
    left(10)
    write("Sola!")
def sagaDon():
    right(10)
    write("Sağa!")
def gitIleri():
    forward(20) #20 birim ilerle
# Tuş fonksiyonları
onkeypress(solaDon, 'Left') #sol ok tuşu
onkeypress(sagaDon, 'Right') #sağ ok tuşu
onkeypress(gitIleri, 'Up') #yukarı ok tuşu
listen() #basılan tuşu dinle
mainloop() #olay yakalama döngüsü
