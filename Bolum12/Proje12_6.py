"""
Proje 12.6. 
Çizgi rengi kırmızı, iç rengi sarı olacak şekilde bir kare çizen programı kodlayalım. 
"""
from turtle import *
#kare çizen fonksiyon
def kareCiz():
    for x in range(4):
        forward(100)
        left(90)
#çizgi rengi kırmızı, içi sarı
color ("red", "yellow")
#şeklin içini de boya
begin_fill()
kareCiz()
end_fill()
