#Proje10_4: Sayıyı roma rakamına dönüştüren fonksiyon
def romaCevir(sayi):
    cikti = "" #şu an için boş
    #sozluk çiftini anahtar ve değeri şeklinde al
    for anahtar, deger in sozluk.items():
        while sayi >= anahtar: #sayi>=anahtar olduğu sürece
            cikti = cikti + deger #değeri çıktıya ekle
            sayi = sayi - anahtar #sayıyı anahtardan çıkar
    return cikti

#Sayıların roma rakam eşdeğerleri:
sozluk = {1000:"M", 900:"CM", 500:"D", 400:"CD",
          100:"C", 90:"XC", 50:"L", 40:"XL",
          10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I" }
sayi = int (input('Sayı.:')) #sayı gir
print (romaCevir(sayi)) #sayıyı çevir ve ekrana yazdır.