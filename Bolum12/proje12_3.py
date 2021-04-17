'''Çocuklar için Python, Bülent Çobanoğlu
proje12_3: Çevirmen-2
'''
def Cevirmen1():
    print ("Ada Konuştu.:")
    S1 = bin (ord("S"))[2:]
    E1 = bin (ord("E"))[2:]
    L1 = bin (ord("L"))[2:]
    A1 = bin (ord("A"))[2:]
    M1 = bin (ord("M"))[2:]
    print (S1,E1,L1,A1,M1)
    
def Cevirmen2():
    print ("Robot Can Konuştu.:")
    S2 = chr(int('1010011', 2))
    E2 = chr(int('1000101', 2))
    L2 = chr(int('1001100', 2))
    A2 = chr(int('1000001', 2))
    M2 = chr(int('1001101', 2))
    print (S2, E2, L2, A2, M2)
#Ana program
Cevirmen1() 
Cevirmen2()