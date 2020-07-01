"""
Bülent Çobanoğlu, Çocuklar için Python
Proje 11.7. 
Bilgisayarın tuttuğu (0-100 arasındaki) sayıya göre kullanıcıyı “daha küçük veya daha büyük sayı giriniz gibi” yönlendiren ve kaç tahminde sayıyı bulduğunu ve puanını söyleyen bir sayı tahmin oyununu kodlayalım. 

"""
import random
#bilgisayar 0-100 arası bir sayı tutar
sayi = random.randint(1,100)
sayac=0
puan=100 
print("İlk Tahmininiz.:");
while True: 
    tahmin =int(input())
    sayac = sayac + 1
    if tahmin == sayi:
        print("Bravo!",sayac,".de bildiniz")
        break #döngüden çık
    elif tahmin < sayi:
        print("Daha büyük bir sayı gir!")
    else:  
        print("Daha küçük bir sayı gir!")
    puan = puan - 10 
print("Puanınız.:",puan)
