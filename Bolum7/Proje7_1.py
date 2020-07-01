"""Çocuklar için Python, Bülent Çobanoğlu
Proje 7.1. Fizz Buzz Oyunu: 
1'den 100'e kadar olan sayıları, sırayla ekrana yazdırılalım. Fakat program; eğer sayı 3 veya 3'ün katıysa, sayı yerine "fizz"; 5 veya 5'in katıysa, sayı yerine "Buzz"; eğer sayı hem 3'ün hem de 5'in (15’in) katıysa, sayı yerine "fizzBuzz" yazmalıdır.
"""
#fizzBuzz fonksiyonu
def fizzBuzz():
    for x in range (1,101):
        if x % 15 == 0:
            print ("fizzBuzz")
        if x % 3 == 0:
            print ("fizz")
        if x % 5 == 0:
            print ("Buzz")
        else:
            print(x, end=' ')
#Ana program
fizzBuzz() #fonksiyon çağrıldı
