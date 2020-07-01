"""
Bülent Çobanoğlu, Çocuklar için Python
Proje 11.8.  
Bilgisayar ile kullanıcı arasında taş-kâğıt-makas oyunu oynayan, kimin ne seçtiğini ve kazananı ekranda gösteren bir programı kodlayalım

"""

import random
Liste = ["Taş", "Kağıt", "Makas"]
#PC için listeden rastgele bir seçim yap
pc = random.choice(Liste) 
#Oyuncunun seçimi 
sen = input('[Taş-Kağıt-Makas]?').capitalize()

#Bilgisayarın seçimi:
print("Bilgisayar:", pc, "seçti") 
#Oyuncunun seçimi:
print("Sen:", sen, "seçtin") 

#9 ihtimal değerlendiriliyor
if pc == sen:
    print ("İkinizde aynı şeyi seçtiniz, Berabere!")
if pc == "Kağıt" and sen == "Makas":
    print ("Makas, kâğıdı keser (Sen kazandın!)")
if pc == "Makas" and sen == "Taş":
    print("Taş, makası kırar (Sen kazandın!)" )
if pc == "Taş" and sen == "Kağıt":
    print("Kâğıt, taşı sarar (Sen kazandın!)" )
if pc == "Makas" and sen == "Kağıt":
    print ("Makas, kâğıdı keser (Bilgisayar kazandı!)")
if pc == "Taş" and sen == "Makas":
    print ("Taş, makası kırar (Bilgisayar kazandı!)")
if pc == "Kağıt" and sen == "Taş":
    print("Kâğıt, taşı sarar (Bilgisayar kazandı)!")
