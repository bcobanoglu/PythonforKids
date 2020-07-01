"""Bülent Çobanoğlu,
Proje 11.6. 
Bir yazar, talihli bir sosyal medya (Twitter) takipçisine son çıkan kitabını hediye edecektir.
Bu yazarın takipçi listesinden rastgele birini seçen programı kodlayalım.

"""
import random
liste = ["@enes", "@can","@ali", "@ada","@eko",
         "@berk","@ela","@alp","@cefa","@vefa"]
#listeden talihli seçiliyor
talihli = random.choice(liste)
print ("Python kitabı çekiliş talihlisi:")
print(talihli)
