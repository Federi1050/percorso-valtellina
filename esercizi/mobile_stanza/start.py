from Dimensione import Dimensione
from Mobile import Mobile
from Stanza import Stanza

dim = Dimensione(12.8,12.9,12.7)

mob1 = Mobile("legno",9.99,dim)
mob2 = Mobile("",9.99,dim)
mob3 = Mobile("legno",9,None)

lista = [mob1, mob2, mob3]

stanza = Stanza("ospedale",lista)
print(stanza)

stanza.rimuovi_mobile(mob2)
print(stanza)
stanza.aggiungi_mobile(mob2)
print(stanza)