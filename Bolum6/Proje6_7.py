"""Bülent Çobanoğlu
Proje 6.7. while True örneği: 
Girilen sayı sıfırdan farklı olduğu sürece o sayının karesini alan programı ‘while True:’ ile yeniden kodlayalım. 

"""
print("Çıkmak için 0 giriniz!")
while True:
    S=int(input('Gir bir sayı.:'))
    print ("Karesi.: ", S*S)
    if (S==0):
        break #döngüden çık
#Döngü sonu
