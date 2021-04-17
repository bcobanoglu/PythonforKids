'''Çocuklar için Python, Bülent Çobanoğlu
Proje 11.1. Araba Sınıfından Yeni Nesneler Üretme
'''
class Araba():
    #Sınıf özelliklerine ilk değerleri atandı
    def __init__(self,marka,model,renk):
        self.marka = marka
        self.model = model
        self.renk = renk

    def aracBilgisi(self):
        print("markası: ",self.marka)
        print("model yılı:", self.model)
        print("rengi:",self.renk)
#Ana program
#Taksi nesnesi oluşturuldu
Taksi = Araba("Honda", 2020, "Gri")
#Kamyonet nesnesi
Kamyonet = Araba ("Ford", 2010, "Beyaz")
#Bu iki nesnenin araç bilgilerini alalım
print ("Taksinin özellikleri.:")  ; Taksi.aracBilgisi()
print ("Kamyonetin özellikleri.:"); Kamyonet.aracBilgisi()