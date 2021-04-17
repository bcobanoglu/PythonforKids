'''Çocuklar için Python, Bülent Çobanoğlu
proje12_7: Sayı Tahmin Oyunu
'''
import random
#Bilgisayar 0-100 arası bir sayı tutar
sayi = random.randint(1,100)
sayac=0
puan=100
print("İlk Tahmininiz.:");
while True:
    tahmin =int(input())
    sayac = sayac + 1
    if tahmin == sayi:
        print("Bravo!", sayac, ".de bildiniz")
        break #döngüden çık
    elif tahmin < sayi:
        print("Daha büyük bir sayı gir!")
    else:
        print("Daha küçük bir sayı gir!")
    puan = puan - 10

print("Puanınız.:",puan)