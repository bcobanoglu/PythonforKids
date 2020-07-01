"""
Proje 5.5.  X sayısının alabileceği değerler (çözüm) kümesi sayı doğrusu üzerinde gösterilmiştir: 12<=x<15

Buna göre girilen X değeri bu aralıkta ise “X sayı doğrusu üzerinde” değilse “X sayı doğrusu üzerinde değil” mesajını ekranda gösteren programı kodlayalım

"""
x=int(input("X değeri.:"))
if (12 <= x < 15):  # Eşdeğeri: (12<=x) and (x<15)
    print ("Sayı doğrusu üzerinde")
else:
    print ("Sayı doğrusu üzerinde değil")
