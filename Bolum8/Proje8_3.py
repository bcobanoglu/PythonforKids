"""Bülent Çobanoğlu
Proje 8.3.
Bir stringin içeriğini (belli bir karakterden sonrasını değiştiren) güncelleyen programı kodlayalım.
"""
ad = 'Refahiye-Hanzar'
yeniAd= ad[:9 ] + 'Teknecik' #Eşdeğeri:ad.replace( 'Hanzar', 'Teknecik')
print ("Güncellendi: ", yeniAd)
