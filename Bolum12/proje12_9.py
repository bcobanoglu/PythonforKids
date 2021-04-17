'''Çocuklar için Python, Bülent Çobanoğlu
proje12_9: Çarpım tablosu oyunu(1-10)
'''
import random
print ("*Çarpım oyunu*\nÇıkmak için sıfır giriniz!!!")
basarili = 0 #başarı durum sayacı
basarisiz = 0 #başarısız durum sayacı
while True:
    a = random.randint(1,10) 
    b = random.randint(1,10) 
    Soru = "{} * {} = ".format(a,b) 
    dCvp = a * b #doğru cevap
    cvp = input(Soru)
    #oyundan çıkma durumu:
    if int(cvp) == 0: #Eğer cevap sıfır girilirse
        break 
    if int(cvp) == dCvp:
        basarili +=1
        print("Cevap doğru!")
    else:
        basarisiz +=1
        print("Cevap hatalı")

#Test durumu
if basarili > basarisiz:
    print ("Tebrikler, çarpman iyi!")
else:
    print ("Üzgünüm, ezber yapman gerek.")