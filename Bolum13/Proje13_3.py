"""Bülent Çobanoğlu, Çocuklar için Python
Proje 13.3. Klavyeden space (uzun çubuk) tuşuna basıldıkça durum değiştiren bir trafik ışık sistemini kodlayalım.
"""
from turtle import *
setup(300, 600)#çerçeve boyutu
title("Trafik ışıkları!") #çerçeve başlığı
pensize(3) #çizim kalemi uç kalınlığı
trfkDurum = 0#Yeşil(0),Sarı(1),Kırmızı(2) 
#dikdörtgen levhayı çizen fonksiyon
def levhaCiz():
    for i in range(2): 
        forward(80)  #kısa kenar
        left(90)
        forward(225) #uzun kenar
        left(90)
#Işık geçişlerini sağlayan fonksiyon
def durumMakinesi():
    global trfkDurum #global değişken
    #0’dan 1’e geçiş işlemi
    if trfkDurum == 0: 
        forward(60) #ileri 60 adım git
        fillcolor("yellow")#ışığı sarı yap
        trfkDurum = 1 #durumu değiştir
    #1’den 2’ye geçiş işlemi
    elif trfkDurum == 1: 
        forward(60) #ileri 60 adım git
        fillcolor("red") #ışığı kırmızı yap
        trfkDurum = 2 #durumu değiştir
    # 2’den 0’a geçiş işlemi
    else: 
        back(120) #geri 120 adım git
        fillcolor("green") #ışığı yeşil yap
        trfkDurum  = 0 #durumu değiştir 
#Ana program
levhaCiz()#levhaCiz fonk. çağrıldı
penup()#kalemi kaldır
goto(40,40) #lambayı konumlandır
left(90) #sola dön
fillcolor("green")#ilk önce yeşil
shape("circle")#Lamba şeklini seç
shapesize(3) #lambanın büyüklüğü
#Işık geçişleri için space tuşuna bas
onkey(durumMakinesi, "space")
listen() #Olayları dinle    
mainloop() #Olay yakalama döngüsü