"""
Bülent Çobanoğlu, Çocuklar için Python
Proje 9.8. 
Kuyruğa eleman ekleme ve çıkarma işlemlerini liste fonksiyonlarını kullanarak gerçekleştirelim.

"""
L = [3, 4]  # Liste
L.append(5) # 5 eklendi
L.append(6) # 6 eklendi
print (L)   # Kuyruk listesi   
bas = L.pop(0)    # 3 ayrıldı
print ("Kuyruktan ayrılan: ", bas)
#Kuyruğun mevcut durumu
print (L)
#Kuyruğun en başındaki eleman
print ("Şimdi en baştaki eleman:", L[0])
