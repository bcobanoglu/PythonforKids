"""Çocuklar için Python kitabı, Bülent Çobanoğlu
Proje 7.2.  
Aşağıdaki gibi dikdörtgen şeklindeki bir tarlanın çevresini ve alanını hesaplayan programı kodlayalım.
--------
|      |
--------
"""
#Alanı hesaplayan fonksiyon
def Alan(u,g):
    a = u * g
    return a
#Çevreyi hesaplayan fonksiyon
def Cevre(u,g):
    c = 2*u +2*g
    return c

#Ana program
u = int (input('Tarlanın uzunluğu:'))
g = int(input('Tarlanın genişliği:'))
print ("Tarlanın Alanı.:", Alan(u,g))
print ("Tarlanın Çevresi.:", Cevre(u,g))
