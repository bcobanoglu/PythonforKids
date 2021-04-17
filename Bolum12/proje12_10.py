'''Çocuklar için Python, Bülent Çobanoğlu
Proje12_10: Hangman oyunu
'''
from random import choice
liste = ["python", "swift", "java", "ruby", "php", "basic", "javascipt", "cobol", "scratch", "delphi" ]
#Listeden rasgele bir kelime seç
hangman = ['''
             +-+
             O |
            /|\|
            / \|
              === ''','''
             +-+
             O |
            /|\|
            /  |
             === ''','''
             +-+
             O |
            /|\|
               |
              === ''',''' 
             +-+
             O |
            /| |
               |
              === ''','''
             +-+
             O |
             | |
               |
              === ''','''
             +-+
             O |
               |
               |
              === ''','''
             +-+
               |
               |
               |
              === ''']
kelime = choice(liste)
dogruHarf = []
yanlisHarf = []
hak = len(hangman)
while hak > 0:
    out = ""
    for h in kelime:
        if h in dogruHarf:
            out = out + h
        else:
            out = out + "_"
    if out == kelime:
        break

    print("Kelime: ", out)  
    #print(hak, "hak kaldı")
    print (hangman[hak-1])
    girHarf = input()
    if girHarf in dogruHarf or girHarf in yanlisHarf:
        print("Zaten ", girHarf, "girilmişti")
    elif girHarf in kelime:
        print("Doğru")
        dogruHarf.append(girHarf)
    else:
        print("Yanlış")
        hak = hak - 1
        yanlisHarf.append(girHarf)

if hak!=0:
    print("Tebrikler, Evet : ", kelime)
else:
    print("Maalesef kelimemiz : ", kelime)
