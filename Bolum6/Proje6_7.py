"""Çocuklar için Python, Bülent Çobanoğlu
Proje 7. 
Dört işlem (toplama, çıkarma, çarpma ve bölme) yapan basit bir hesap makinesi uygulamasını 
kullanıcının devam etmek isteyip/istememesine göre kodlayalım. 
"""
while True:
    s1 = int(input('sayı1.:'))
    s2 = int(input('sayı2.:'))
    op = input('işlem.:')
    if (op == '+'):
        S = s1 + s2
    elif (op == '-'):
        S = s1 - s2
    elif (op == '*'):
        S = s1 * s2
    elif (op == '/'):
        S = s1 / s2
    else:
        print("Hatalı seçim")    
    print("Sonuç=",S)
    cvp=input("Başka işlem olacak mı[e/h]?")
    if cvp=='h':
        break
    else:
        continue
print("..Makine kapandı..")


