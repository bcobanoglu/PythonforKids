"""Çocuklar için Python kitabı, Bülent Çobanoğlu
Proje 7.3. 
Ana programda (main fonksiyonunda) girilen Fahrenhayt sıcaklığını (F°) cevir isimli fonksiyonla Dereceye (C°) çeviren ve çevrim sonucunu ana programda gösteren programı yazalım. 

"""
#cevir fonksiyonu
def cevir(f):
    return ((f - 32) / 1.8)
#Ana program
f=float(input('Fahrenhayt değeri:'))
C = cevir(f)
print(C , " derecedir")
