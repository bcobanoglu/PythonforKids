'''Çocuklar için Python, Bülent Çobanoğlu
Proje 14.2. Yön Tuşları ile Çizim Yapma
Grafik ekranına klavyedeki yön tuşlarını kullanarak çizim yapan programı kodlayalım
'''
from turtle import *
shape('turtle') #Kaplumbağa şekli: 'turtle'
pensize(3) #Kalem kalınlığı
wn = Screen() #wn:Ekran değişkeni
#Artık program içerisinde Screen() nesnesi yerine ‘wn’ kullanılacak
wn.setup(300,300) #Çizim ekranı çerçeve boyutu
#Yön tuşları için tanımlanan fonksiyonlar:
def solaDon():
  left(90) #Sola 90 derece dön
  write("Sola!") #Yaz ‘Sola’
def sagaDon():
  right(90) #Sağa 90 derece dön
  write("Sağa!") #Yaz ‘Sağa’
def gitIleri():
  forward(20) #20 birim ilerle


#Sola yön okuna basıldığında ‘solaDon’ fonksiyonunu çalıştır
wn.onkeypress(solaDon, 'Left')
#Sağa yön okuna basıldığında ‘sagaDon’ fonksiyonunu çalıştır
wn.onkeypress(sagaDon, 'Right')
#Yukarı yön okuna basıldığında ‘gitIleri’ fonksiyonunu çalıştır
wn.onkeypress(gitIleri, 'Up')
#Yukarı yön oku
wn.listen() #Hangi tuşa basıldığını dinle?
wn.mainloop() #Olay yakalama döngüsünü başlat
