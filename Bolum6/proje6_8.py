"""Proje 6.8. Sonsuz Döngü: Trafik Sinyalizasyon Sistemi
"""
# Trafik Lambası Programı
while True:
    Lamba = input('Trafik Lambası rengi.:')
    if (Lamba=='K'):
        print ("Bekle")
    if (Lamba=='S'):
        print ("Yavaşla")
    if (Lamba=='Y'):
        print ("Geç")
        break #döngüden çık
#Döngü sonu