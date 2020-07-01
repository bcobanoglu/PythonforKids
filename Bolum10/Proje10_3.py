"""Bülent Çobanoğlu,
Proje 10.3. 
İl plakalarını tutan bir sözlük yapısı oluşturarak sözlüğe yeni eleman ekleme, silme ve sorgulama işlemlerinin nasıl yapılacağını gösteren bir program yazalım.

"""
plaka = {} #boş plaka sözlüğü tanımlandı
#plaka sözlüğüne elemanlar ekleniyor
plaka['01']='Adana'
plaka['06']='Ankara'
plaka['16']='Bursa'
plaka['24']='Erzincan'

#plaka sorgulaması yapıldı
print("01 plakalı il.:", plaka.get('01'))
#plaka silindi
plaka.pop('01') #01 plakalı il silindi
#Tekrar plaka sorgulaması yapıldı
print("01 plaka silindi.:", plaka.get('01'))
