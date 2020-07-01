"""
Çocuklar için Python
Proje 6.4. 
1’den 100’e kadar olan tek sayıların toplamını bulan programı kodlayalım.
"""
a = 1
Top = 0 #Toplama değişkeni
while a <= 100:
    Top = Top + a #Yığmalı toplama
    a = a + 2
#Döngü sonu
print ("Toplam=",Top)
