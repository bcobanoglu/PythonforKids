""" Çocuklar için Python, Bülent Çobanoğlu
Proje 5.6. Park Ücreti
"""
Saat = float(input('Kalma Süresi.: '))
if Saat <= 2:
	Ucret = 5
elif Saat <= 5:
	Ucret = 10
else:
	Ucret = 15
print ("Park Ücreti.:", Ucret, "TL")
