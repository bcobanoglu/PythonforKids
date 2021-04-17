from turtle import *
title ("Türk Bayrağı")      #çerçeve başlığı yazısı
setup(width=600,height=400) #çerçeve boyutu
bgcolor("red")              #çerçeve arka plan rengi:kırmızı 
hideturtle()                #turtle nesnesini gizleyelim

def renkveKonum(renk, x, y):        #konumlanma fonksiyonu:
    penup()                 #çizim kalemini kaldır
    goto(x, y)              #konumlan
    pendown()               #kalemi tekrar koy
    color(renk)             #boyama rengi: renk değişkeni
    begin_fill()            #boyamaya başla

def yildiz():               #Yıldız çizen fonksiyon:
    renkveKonum("white",80,25)  #Önce konumlan
    for i in range(5):      #Sonra döngü içerisinde 5 kez
        forward(50)         #ileri 50 adım git
        right(144)          #144 derece sağa dön
        forward(50)         #ileri 50 adım git
        right(-72)          #-72 derece sağa dön
    end_fill()              #boyamayı sonlandır

def ay(cap):                #ay çizen fonksiyon:
    circle(cap)             #daire çiz
    end_fill()              #boyamayı sonlandır

#Ana program
renkveKonum("white",-110,-120)  #konum fonksiyonunu çağıralım
ay(130)                         #beyaz daire çizelim
renkveKonum("red", -70, -90)    #konumu ve rengi değiştirelim
ay(100)                         #kırmızı daire çizelim
#iki daire farklı renklere boyanarak hilal şekli elde edilmiş oldu.
yildiz()                        #yıldız çizim fonksiyonunu çağıralım
mainloop()                      
#Çizim ekranının kaybolmaması için mainloopu hep çağıralım.
