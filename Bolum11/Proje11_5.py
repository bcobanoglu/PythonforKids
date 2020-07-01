"""
Proje 11.5. 
Bilgisayarın rastgele ürettiği 1-49 arasındaki 6 adet sayıyı sayısal loto çekiliş sonucu olarak ekrana yazan programı kodlayalım. 

"""
#sayısal loto
import random
print("Sayısal Loto Çekilişi\n") 
#6 adet
for i in range (6):
    #1-50 arası sayı üret
    sL=random.randint(1,49)
    #sayıları yan yana yaz
    print (sL, end=' ')
