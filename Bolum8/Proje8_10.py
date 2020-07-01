"""
Çocuklar için Python
Proje 8.10. 
Bir metindeki sesli ve sesiz harf sayısını hesaplayan programı kodlayalım. 

"""
cumle="Devletin dini adalettir."
sesli = "aeıiouü"
sessiz = "bcçdfgğhjklmnprsştvyz"
sayac1=sayac2=0
for harf in cumle.lower():
    if harf in sesli: 
        sayac1 = sayac1 + 1 
    if harf in sessiz: 
        sayac2 = sayac2 + 1 

print ("Sesli harf sayısı: ", sayac1)
print ("Sessiz harf sayısı: ", sayac2)
