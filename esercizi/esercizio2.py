#dati in input 2 numeri dai il risultato delle operazioni matematiche base tra i due

numero1 = input("Inserisci il primo numero: ")
numero1 = int(numero1)
# puoi anche fare = int(input("blabla"))
numero2 = input("Inserisci il secondo numero: ")
numero2 = int(numero2)

risultato = numero2 + numero1
print("somma:",risultato)
# direttamente nel print -> print(numero1 + numero2)
risultato = numero1*numero2
print("moltiplicazione:",risultato)
risultato = numero1-numero2
print("sottrazione:",risultato)
risultato = numero1/numero2
print("divisione:",risultato)