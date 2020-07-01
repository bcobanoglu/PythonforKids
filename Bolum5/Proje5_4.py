"""
Proje 5.4. 
Girilen kullanıcı adı (user) ve parola (password) bilgilerine göre “Hoş geldiniz!” değilse ‘hatalı kullanıcı adı veya parola’ girişi mesajı veren programı kodlayalım. 
"""
user = input('Kullanıcı Adı.:')
password = input('Parola.:')
if user == 'admin' and password=='admin':
    print ("Hoş geldiniz!")
else:
    print ("Hatalı kullanıcı adı veya parola girişi")
