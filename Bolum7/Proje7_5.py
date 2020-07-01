"""Çocuklar için Python kitabı, Bülent Çobanoğlu
Proje 7.5.
Aşağıda sol sütunda çalışma mantığı verilen 2 sayısının N. üssünü alan programı özyinele-meli fonksiyon yapısında kodlayalım. 

"""
#Özyinelemeli Us fonksiyonu
def Us(N):
    if N==0:
        return 1 
    else:
        return 2*Us(N-1)

#Ana program
N = 5
print (Us(N))
