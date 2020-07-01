"""
Çocuklar için Python
Proje 12.4. 
Bir kaplumbağa robotu, merdivenden 5 basamak aşağı indiren (veya 5 basamaklı bir merdiven şeklini ekrana çizen) uygulamayı kodlayalım. 

"""
from turtle import *
shape ("turtle")
for i in range(1, 5):
    forward(50)
    right(90)
    forward(50)
    left(90)