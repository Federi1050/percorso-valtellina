#crea una semplice funzione
#crea una semplice funzione che prende in input una lista di boolean: 
#ritorna True se tutti elementi sono True altrimenti False

def saluta(name : str):
    print(f"ciao {name}")

def allTrue(lista : list):

    if len(lista) == 0:
        return False
    for elemento in lista:
        if elemento == False: # elemento is False
            return False
    return True
        

saluta("Franco")
my_lista = [True, True, True, True]
print(allTrue(my_lista))