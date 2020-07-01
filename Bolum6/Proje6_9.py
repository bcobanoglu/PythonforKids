"""
Proje 9. Çıktı deseni oluşturma: 
Yandaki(Çıktıdaki) dik üçgen desenini ekrana basacak/yazacak programı iç içe döngü kullanarak  kodlayalım.
"""
#dıştaki döngü: m
for m in range (1,6): 
    #içteki döngü: n
    for n in range(m): 
        print("#", end = '')
    #içteki döngü sonu
    print() #bir satır atla
#dıştaki döngü sonu
