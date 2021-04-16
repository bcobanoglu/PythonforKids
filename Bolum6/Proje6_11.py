"""Çocuklar için Python, Bülent Çobanoğlu
Proje 11. Çıktı deseni oluşturma:
Dik üçgen desenini ekrana basacak/yazacak programı iç içe döngü kullanarak  kodlayalım.
"""
#dıştaki döngü: m
for m in range (1,6): 
    #içteki döngü: n
    for n in range(m): 
        print("#", end = '')
    #içteki döngü sonu
    print() #bir satır atla
#dıştaki döngü sonu
