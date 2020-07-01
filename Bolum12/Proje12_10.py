"""Çocuklar için Python 
Proje 12.10. 
30 birim yarıçaplı, 150*100 çerçeve içerisinde bir Japon bayrağı çizelim.
"""
#japon bayrağı
from turtle import *
shape('blank')
pensize(5) #kalın çerçeve
#dikdörtgen çerçeveyi çiz
for i in range(2): 
  forward(150)
  right(90)
  forward(100)
  right(90)

pencolor("red") #kalem rengi

penup() #kalemi kaldır
goto (75,-80) #daire çizimi için konumlan
pendown()#kalemi koy
fillcolor("red") #içini kırmızıya boya
begin_fill() #boyama başla
circle(30) #yarıçapı:30 olan daireyi çiz
end_fill() #boyamayı bitir
