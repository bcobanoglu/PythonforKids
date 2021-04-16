#Proje9_7: Haftanın günleri
gun= ['Pazartesi', 'Salı', 'Çarşamba',
'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
#enumerate() ile indisini ve değerini aldık
for i, deger in enumerate(gun):
    #print (str(i+1) + ".gün: " + deger)
    print (i+1, ".gün: ", deger)