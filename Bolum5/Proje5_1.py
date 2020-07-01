"""Çocuklar için Python, Bülent Çobanoğlu
Proje 5.1.  
Klavyeden girilen sayıları ekranda gösteren  (eğer girilen sayı sıfırdan küçükse sayının karesini alan) programı kodlayalım.
"""
S = int (input('Gir bir sayı.:'))
if S<0:
    S=S*S
print (S)
