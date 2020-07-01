"""Herkes için Python, Bülent Çobanoğlu
Proje 6.5. 
A dan Z ye kadar İngilizce karakterleri ekranda gösteren programı while döngüsü ile kodlayalım.
Not. ASCII kod tablosunda yer alan karakterleri ve sayısal değerlerin tamamını görmek için
http://www.asciitable.com/ adresini inceleyebilirsiniz.
"""
k = ord('A') #k=65 oldu
while k<=ord('Z'):
    #chr(65) = 'A' demektir
    print (chr(k), end=' ')
    k = k + 1
