"""
Proje 5.2. 
Girilen bir sayının sıfır mı, negatif mi veya pozitif mi olduğunu ekranda gösteren programı kodlayalım.
"""
S = int(input('Gir bir sayı.:'))
if S<0:
    print("Sayı Negatif")
if S>0:
    print("Sayı Pozitif")
if S==0:
    print("Sayı Sıfır")
