"""Çocuklar içn Python kitabı,
Proje 9.1.
Kullanıcı tarafından girilen 5 adet sayıyı A listesine aktarıp, şekildeki gibi ekranda gösteren programı kodlayalım.

"""
A = [] #boş liste
for i in range(0,5):
    sayi = int(input('Sayı.:'))
    A.append(sayi) #girilen sayıyı listeye ekle
#döngü sonu

#Liste elemanlarını alt alta yazdıralım
for i in range(0,5):
    print ("A[", i, "]=",A[i])
#döngü sonu   

