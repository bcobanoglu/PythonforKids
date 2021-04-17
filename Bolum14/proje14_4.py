"""
Bülent Çobanoğlu, Çocuklar için Python
Proje 13.4.  Eski telefonların vazgeçilmez oyunu olan ‘yılan oyununu’ Turtle ile adım adım kodlayalım. 
"""
import turtle
import time, random
skor = 0 ; maxSkor = 0 
Liste = [] 
#Oyun ekranı(çerçevesi) ayarları:
wn = turtle.Screen()
wn.title("Yılan oyunu")
wn.bgcolor("green") 
wn.setup(600, 600) 
wn.tracer(0) 
#Yılan başı nesnesi ayarları:
yln= turtle.Turtle()
yln.speed(0) 
yln.shape("square") 
yln.color("yellow") 
yln.penup() 
yln.goto(0, 100) 
yln.yonu = "dur" 
#Yem nesnesi ayarları:
yem = turtle.Turtle()
yem.speed(0) 
yem.shape("circle") 
yem.color("white") 
yem.penup()
yem.goto(0,0) 
#Hareket fonksiyonu:
def Hareket():
    if yln.yonu == "ust":
        y = yln.ycor() 
        yln.sety(y + 20) 
    if yln.yonu == "alt":
        y = yln.ycor() 
        yln.sety(y - 20) 
    if yln.yonu == "sag":
        x = yln.xcor()
        yln.setx(x + 20) 
    if yln.yonu == "sol":
        x = yln.xcor()
        yln.setx(x - 20) 
#Yön tuşları fonksiyonları:
def gitYukari():
    if yln.yonu != "alt":
        yln.yonu = "ust"
def gitAsagi():
    if yln.yonu != "ust":
        yln.yonu = "alt"
def gitSaga():
    if yln.yonu != "sol":
        yln.yonu = "sag"
def gitSola():
    if yln.yonu != "sag":
        yln.yonu = "sol"
#Tuş olaylarını yakala;
wn.listen()
wn.onkeypress(gitYukari, "Up") 
wn.onkeypress(gitAsagi, "Down") 
wn.onkeypress(gitSaga, "Right")
wn.onkeypress(gitSola, "Left")

#yemiYe() fonksiyonu:
def yemiYe(): 
   global skor, maxSkor
   if yln.distance(yem)<20: 
      x = random.randint(-280, 280)
      y = random.randint(-280, 280) 
      yem.goto(x, y) 
      #kuyruk nesnesi ayarları:
      kuyruk = turtle.Turtle()
      kuyruk.speed(0) 
      kuyruk.shape("square") 
      kuyruk.color("red") 
      kuyruk.penup() 
      Liste.append(kuyruk) 

      skor = skor + 10
      if skor > maxSkor:
         maxSkor = skor

      wn.title("Skor: {}  En yüksek skorun: {}".format(skor, maxSkor))

   uz = len(Liste)
   for indis in range(uz-1, 0, -1): 
      x = Liste[indis-1].xcor() 
      y = Liste[indis-1].ycor() 
      Liste[indis].goto(x, y)

   if len(Liste) > 0: 
      x = yln.xcor() 
      y = yln.ycor()
      Liste[0].goto(x,y) 
#baslangicAyarlari() fonksiyonu:
def baslangicAyarlari():
    time.sleep(1) 
    yln.goto(0,0) 
    yln.yonu = "dur"
    global skor
    for eklem in Liste:
        eklem.goto(1000, 1000)
    Liste.clear() 
    skor = 0 
    wn.title("Skor: {}  En yüksek skorun: {}".format(skor, maxSkor))
#Ana program sonsuz döngüsü:
while True:
   wn.update()
   yemiYe()
   Hareket()    
   if yln.xcor()>290 or yln.xcor()<-290 or yln.ycor()>290 or yln.ycor()<-290:
      baslangicAyarlari()
   for eklem in Liste:
      if eklem.distance(yln) < 20:
         baslangicAyarlari()
   time.sleep(0.1) 
#olay yakalama döngüsü aktif
wn.mainloop()