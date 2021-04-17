"""Bülent Çobanoğlu,
Proje 14.1.  Grafik ekrana mouse (fare) tıklaması ile çizim yapan programı kodlayalım.
"""
from turtle import *
pensize(3) #çizim kalemi kalınlığı
wn = Screen()#wn:ekran değişkeni
#Artık program içerisinde Screen() nesnesi yerine ‘wn’ kullanılacak
wn.setup(200,200) #Çizim ekranı boyutu
#Koordinatı bulan fonksiyon
def Nokta(x, y):
   goto(x, y) #tıklanılan yere git
#Click olayı
wn.onclick(Nokta)
mainloop() #olay yakalama döngüsü: çizimin ekranda kaybolup gitmesine mani olur.
