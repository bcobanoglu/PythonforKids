"""Çocuklar için Python
Proje 7.7. Hanoi kuleleri oyunu: 
"""
def Hanoi(n, A, C, B):
    global s #s global bir değişken
    if n>0:
        Hanoi(n-1, A, B, C)
        print(s,".adim:",A,"-->",C)
        s=s+1
        Hanoi(n-1, B, C, A)
        return
#ana program
n = int(input('n degeri.:'))
s = 1	
#Hanoi(n, 'kaynak', 'hedef', 'yedek')
Hanoi(n, 'A', 'C', 'B')
