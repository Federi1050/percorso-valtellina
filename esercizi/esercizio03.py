# costruire semplice programma che prende in ingresso un numero usando la funzione 
# di input e restituisce pari o dispari

numero = int(input("inserisci un numero: "))
if numero%2==0:
    print("Il numero è pari")
else:
    print("Il numero è dispari")

parita = "pari" if numero%2 == 0 else "dispari"
print(parita)