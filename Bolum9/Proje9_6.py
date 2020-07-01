"""Çocuklar için Python, Bülent Çobanoğlu
Proje 9.6. 
Bir string ifadeyi listeye dönüştürüp liste elemanlarını küçükten büyüğe doğru kabarcık sıralama (bublesort) algoritmasına göre sıralayan programı kodlayalım.

"""
#kabarcık sıralama algoritması
def benimSort(A):
    n = len(A) #A listesinin eleman sayısı
    for a in range (0,n):
        for b in range (a+1,n):
            if A[a]>A[b]:
                #yer değiştir
                A[a], A[b] = A[b], A[a]
#Ana program
S = "6539421"
A = list(S)
benimSort(A)  #A listesini sırala 
print (A) #sıralı hali ekrana yaz

