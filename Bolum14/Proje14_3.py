"""Bülent Çobanoğlu, Çocuklar için Python
Proje 14.3. Klavyeden space (uzun çubuk) tuşuna basıldıkça durum değiştiren bir trafik ışık sistemini kodlayalım.
"""
from turtle import *
wn = Screen() #wn:Ekran değişkeni
#Artık program içerisinde Screen() nesnesi yerine ‘wn’ kullanılacak
wn.setup(300,600) #Çizim ekranı çerçeve boyutu
wn.title("Trafik ışıkları!") #çerçeve başlığı
pensize(3) #çizim kalemi uç kalınlığı
#Trafik durumunu gösteren değişken: trfkDurum
#Yeşil: 0, Sarı: 1, Kırmızı: 2
trfkDurum = 0
#Dikdörtgen levhayı çizen fonksiyon
def levhaCiz():
    for i in range(2):
        forward(80) #kısa kenar
        left(90)
        forward(220) #uzun kenar
        left(90)
#Lambayı çizen fonksiyon
def lambaCiz():
    penup() #çizim kalemini kaldır
    goto(40,40) #çizim için 40,40 koordinatlarına konumlan
    left(90) #sola dön
    fillcolor("green") #ilk önce ışığı yeşil yap
    shape("circle") #Lamba şeklini seç
    shapesize(3) #lambanın büyüklüğü

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
levhaCiz()#levhaCiz fonksiyonu çağrıldı
lambaCiz()#lambaCiz fonksiyonu çağrıldı
#Işık durum geçişleri fonksiyonu için space tuşuna bas
wn.onkey(durumMakinesi, "space")
wn.listen() #Olayları dinle
wn.mainloop() #Olay yakalama döngüsünü başlat
