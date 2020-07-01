"""
Proje 12.8. 
Ekrana çizgi rengi kırmızı, dolgu rengi sarı bir yıldız çizen programı kodlayalım. 
"""
#Yıldız çizimi
from turtle import *
shape('blank') #ok kullanma
pensize(3) #çizgi kalınlığı
pencolor("red") #çizgi rengi
fillcolor("yellow") #dolgu rengi
begin_fill() #boyama başla
for i in range(5):
    forward(100)
    right(144)
end_fill() #boyamayı bitir
