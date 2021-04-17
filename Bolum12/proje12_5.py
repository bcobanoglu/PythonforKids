'''Çocuklar için Python, Bülent Çobanoğlu
proje12_5: Sayısal Loto Oyunu
'''
import random
print("Sayısal Loto Çekilişi\n")
#6 adet random sayı üret
for i in range (6):
    #1-50 arası sayı üret
    sL=random.randint(1,49)
    #sayıları yan yana yaz
    print (sL, end=' ')