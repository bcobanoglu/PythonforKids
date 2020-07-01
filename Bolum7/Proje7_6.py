"""
Proje 7.6. 
OBEB’i hesaplama: Öklid Algoritmasına göre iki tam sayının OBEB' ini hesaplayan programı kodlayalım.

"""
def OBEB(a, b):
    if (a == 0):
        return b
    else:
        return OBEB(b%a, a); 
#Ana program
A = int(input("A sayısı.:"))
B = int(input("B sayısı.:"))
print ("OBEB= ", OBEB (A,B))
