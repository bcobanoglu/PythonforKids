"""
Proje 12.14.
Bilgisayarda yüklü bir resmi (“kralTakim.gif”) grafik ekranın arka plan resmi olarak ayarlayan programı kodlayalım.
"""
from turtle import *
#resim çerçeve boyutu
setup(400, 800)
#resim dosyası .gif formatında
bgpic("enKralTakim.gif")
#çerçeve başlığı
title("En Kral Takım")
mainloop()