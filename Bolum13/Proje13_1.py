"""Bülent Çobanoğlu,
Proje 13.1.  Grafik ekrana mouse (fare) tıklaması ile çizim yapan programı kodlayalım.
"""
from turtle import *
pensize(3) #çizim kalemi kalınlığı
wn = Screen()#wn:ekran değişkeni
wn.setup(200,200) #Çizim ekranı boyutu
#Koordinatı bulan fonksiyon
def Nokta(x, y):
   goto(x, y) #tıklanılan yere git
#Click olayı
wn.onclick(Nokta)
#olay yakalama döngüsü
mainloop()
