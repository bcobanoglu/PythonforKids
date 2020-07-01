"""Çocuklar için Python kitabı: Bülent Çobanoğlu
Proje 9.4. 
Bir A listesinde aranan sayı varsa sayının listedeki yerini ve sırasını veren programı kodlayalım.

"""
A = [2, 3, 5, 8, 9, 12, 34, 6, 7]
Ara=int(input("Aranan Sayı: "))
if Ara in A:#True ise
    i=A.index(Ara)#Arananin indisi
    print("Aranan", i+1, ". sırada bulundu")
else:#False ise
    print ("Aranan bulunamadı.")
