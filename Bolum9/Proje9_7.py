""" Bülent Çobanoğlu, Python for Kids
Proje 9.7. 
Yığına eleman ekleme ve çıkarma işlemlerini liste fonksiyonlarını kullanarak gerçekleştirelim.

"""
L = [3, 4] #Liste
L.append(5) #5 eklendi
L.append(6) #6 eklendi
#Mevcut yığın yapısı
print (L) 
#Yığının tepesindeki eleman çıkarıldı
ust = L.pop()
print ("Yığından çıkarılan: ", ust)
#Yığının mevcut durumu
print (L)
#Yığının en üstündeki eleman
print ("Şimdi en tepedeki eleman:", L[-1])

