#Verilen Para miktarı:
Miktar = 69          #TL
ceyrek = Miktar // 25#çeyrek hesabı
Miktar = Miktar % 25 #kalan
onluk = Miktar // 10 #onluk hesabı
Miktar = Miktar % 10 #kalan
beslik = Miktar // 5 #beşlik hesabı
Miktar = Miktar % 5  #birlik hesabı
#Değişken değerleri ekrana yazdırılıyor
print(ceyrek, "Çeyrek") #2 Çeyrek
print(onluk, "Onluk")   #1 Onluk
print(beslik, "Beşlik") #1 Beşlik
print(Miktar, "Birlik") #4 Birlik