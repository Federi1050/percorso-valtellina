# distributore con bibite dove ogni bibita e' un elemento
# se presente rimuovi bibita
# valore totale bibite

from Bibita import Bibita
from Distributore import Distributore

'''
bibita = Bibita()
print(bibita)
bibita = Bibita("",-9.9)
print(bibita)
bibita = Bibita("coca cola", 1.10)
print(bibita)
'''
bibita1 = Bibita("Fanta", 1.20)
bibita2 = Bibita("Sprite", 1.15)
bibita3 = Bibita("Tè al limone", 1.50)
bibita4 = Bibita("Acqua naturale", 0.80)
bibita5 = Bibita("Succo d'arancia", 1.70)

'''
dis = Distributore()
print(dis)
dis = Distributore(-8, ["mmm","mmm"])
print(dis)
'''
dis = Distributore(8)
print(dis)

print("########################")
if dis.add_bevanda(bibita1): 
    print("inserimento riuscito")
else:
    print("ups")
if dis.add_bevanda(bibita4):
    print("inserimento riuscito")
else:
    print("ups")
if dis.add_bevanda(bibita3):
    print("inserimento riuscito")
else:
    print("ups")

print(dis)

print(dis.somma_totale_bevande())
print(dis.valore_totale_bevande())

print("no soldi")
print(dis.eroga_bevanda(bibita1,0.8))
print("no bibita")
print(dis.eroga_bevanda(bibita2,100.8))
print("ok")
print(dis.eroga_bevanda(Bibita("Fanta", 1.20),50))
print("dis dopo modifiche")
print(dis)

a = [1,2,3,4,5]
print(a)