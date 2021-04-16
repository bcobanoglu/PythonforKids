"""Çocuklar için Python,Bülent Çobanoğlu
Proje 10.5. Tic-Tac-Toe (XOX) Oyunu
Tic-Tac-Toe (XOX) Oyununu sözlük yapısını kullanarak kodlayalım.
"""
#1.Tic-tac-toe tahta yerleşim şeklini çizdirelim:
print ("1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9")
#Tahta sözlük yapısının anahtar ve değerlerine atama yapılıyor
tahta = {'1': '', '2': '', '3': '',
         '4': '', '5': '', '6': '',
         '7': '', '8': '', '9': ''}

def yazTahta(tahta):
    print(tahta['1'] + '|' + tahta['2'] + '|' + tahta['3'])
    print("-+-+-")
    print(tahta['4'] + '|' + tahta['5'] + '|' + tahta['6'])
    print("-+-+-")
    print(tahta['7'] + '|' + tahta['8'] + '|' + tahta['9'])
    
#3. Oyunu kim kazandı? Olasılıkları yazalım
def kimKazandi(tahta, simge):
    #yan yana kazanma olasılıkları
    if tahta['1'] == tahta['2'] == tahta['3'] == simge:
        return True
    if tahta['4'] == tahta['5'] == tahta['6'] == simge:
        return True
    if tahta['7'] == tahta['8'] == tahta['9'] == simge:
        return True

    #alt alta kazanma olasılıkları
    elif tahta['1'] == tahta['4'] == tahta['7'] == simge:
        return True
    elif tahta['2'] == tahta['5'] == tahta['8'] == simge:
        return True
    elif tahta['3'] == tahta['6'] == tahta['9'] == simge:
        return True

    #çapraz kazanma olasılıkları
    elif tahta['1'] == tahta['5'] == tahta['9'] == simge:
        return True
    elif tahta['3'] == tahta['5'] == tahta['7'] == simge:
        return True
    
    else:
        return False #beraberlik durumu
#2.Simgeleri yerleştir: X ve O ları yerleştir
simge = 'X' #ilk olarak oyuna X başlasın
for i in range(9):
    print(simge + ', nereye yerleştirilsin?')
    gir = input() #simge gir
    tahta [gir] = simge
    if simge == 'X': #simgeyi değiştir
        simge = 'O'
    else:
        simge = 'X'
    yazTahta(tahta) #simgeyi tahtaya yerleştir
    #kimKazandi() fonksiyonundan gelen sonuca göre ekrana mesaj yaz
    if kimKazandi(tahta, 'X'):
        print("Oyunu X Kazandı")
        break
    if kimKazandi(tahta, 'O'):
        print("Oyunu O Kazandı")
        break
    
#beraberlik durumunda ki mesajı yazalım
if kimKazandi(tahta, 'O') == False and kimKazandi(tahta, 'X')==False:
    print("Berabere..")
