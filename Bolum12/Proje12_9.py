"""Çocuklar için Python
Proje 12.9. 
Saat yönünün tersinde hareket ederek yarıçapı 50 birim ve dolgu/iç rengi kırmızı olan bir daire çizelim.

"""

from turtle import *
pensize(3) #kalın uç
#kalem: siyah, iç dolgu: kırmızı renkli
color("black", "red")
begin_fill() #boyama başla
circle(50) #yarıçapı:50
end_fill() #boyamayı bitir	 

