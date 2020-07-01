""" Çocuklar için Python
Proje 8.9.
Girilen bir metnin Palindrom olup olmadığını sorgulayan programı kodlayalım.

"""

s=input("Bir metin gir.:")
if s == s[::-1]:
    print(s, ":palindrom")
else:
    print(s, ":palindrom degil")
