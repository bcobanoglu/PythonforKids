'''Çocuklar için Python, Bülent Çobanoğlu
proje12_8: Taş-Kağıt-Makas Oyunu
'''
import random
Liste = ["Taş", "Kağıt", "Makas"]
pc = random.choice(Liste)
sen = input('[Taş-Kağıt-Makas]?').capitalize()
#Bilgisayarın seçimi:
print("Bilgisayar:", pc, "seçti")
#Oyuncunun seçimi:
print("Sen:", sen, "seçtin")
#ÇOCUKLAR İÇİN PYTHON: Sayfa 154
#9 ihtimal tek tek değerlendiriliyor
if pc == sen: #1
    print ("İkinizde aynı şeyi seçtiniz, Berabere!")
if pc == "Kağıt" and sen == "Makas": #2
    print ("Makas, kâğıdı keser (Sen kazandın!)")
if pc == "Makas" and sen == "Taş": #3
    print("Taş, makası kırar (Sen kazandın!)" )
if pc == "Taş" and sen == "Kağıt": #4
    print("Kâğıt, taşı sarar (Sen kazandın!)" )
if pc == "Makas" and sen == "Kağıt": #5
    print ("Makas, kâğıdı keser (Bilgisayar kazandı!)")
if pc == "Taş" and sen == "Makas":#6
    print ("Taş, makası kırar (Bilgisayar kazandı!)")
if pc == "Kağıt" and sen == "Taş": #7
    print("Kâğıt, taşı sarar (Bilgisayar kazandı)!")
