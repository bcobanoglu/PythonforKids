""" Çocuklar için Python, Bülent Çobanoğlu
Proje 5.6. 
100’lük sisteme göre girilen başarı notunu yanda verilen tabloya göre harfli sisteme çeviren programı kodlayınız. 
"""
Nt=int(input('Gir Notu.: '))
print ("Ders Notu.:")
if Nt >= 90 and Nt<=100:
    print ("A")
elif Nt >= 80 and Nt<=89:
    print ("B")
elif Nt >= 70 and Nt<=79:
    print ("C")
elif Nt >= 60 and Nt<=69:
    print ("D")
elif Nt >= 50 and Nt<=59:
    print ("E")
elif Nt >= 0 and Nt<=49:
    print ("F")
else:
    print ("Lütfen 0-100 arası not giriniz!")

