'''Çocuklar için Python, Bülent Çobanoğlu
Proje 11.2. Kalıtım
'''
#üst sınıf
class anneBaba():
    #başlatıcı metot ve parametreleri
    def __init__(self, renk):
        self.renk = renk
        print ("Göz rengim.:" + self.renk)

class Evlat(anneBaba):
    #başlatıcı metot ve parametreleri
    def __init__(self, renk, alinTerim):
        #anneBaba sınıfından göz rengimi aldım
        anneBaba.__init__(self, renk)
        #kendi alın terim ise diplomam
        self.alinTerim = alinTerim
        print ("Alın terim:" + self.alinTerim)
# Ana program
# Evlat alt sınıfından ‘ali’ nesnesi türetildi
print ("---Ben Ali---")
Ali = Evlat("Ela", "Diploma")