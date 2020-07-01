"""
Çocuklar için Python, Bülent Çobanoğlu
Proje 4.5. 
Fiyatı ve ismi girilen bir ürünün KDV dâhil fiyatını hesaplayan programı kodlayalım. KDV oranı %20 alınacaktır

"""
Urun = input("Ürünün Adı.:")
Fiyat= float(input("Ürünün Fiyatı.:"))
kdvFyt = Fiyat*1.20
print ("Ürün adı.:", Urun)
print ("KDV'li Fiyatı.:", kdvFyt, "TL")
