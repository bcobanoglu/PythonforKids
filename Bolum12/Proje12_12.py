"""
Proje 12.12.
stamp (damga/kaşe) ile ekrana altıgen çizdiren bir programı kodlayalım.
"""
from turtle import *
shape("turtle") #damga şekli 
#360/6 = 60 derece ile 6-gen çizelim 
for i in range(6):
    stamp() #her adımda mevcut damgayı bas
    right(60) #sağa dön
    forward(60) #30 birim ileri git	 
mainloop()

