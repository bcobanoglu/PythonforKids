"""Çocuklar için Python
Proje 8.11. 
Bir metin (cümle) içerisinde aranan kelimenin olup olmadığını sorgulayan bir programı kodlayalım.

"""
cumle="Devletin dini adalettir."
ara = "adalet"
if ara in cumle:
    print ("Evet,", ara, "metinde geçmektedir")
else:
    print ("Hayır,", ara, "metinde geçmemektedir")
