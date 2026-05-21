# utilizzando il while chiede in input un numero e stampi la tabellina di quel numero

numero = int(input("inserisci il numero "))

#controllo che sia almeno positivo
while(numero <= 0):
    print("vorrei un numero maggiore di 0")
    numero = int(input("inserisci il numero "))

print(f"ha inserito {numero}")

i=1
while (i < 11):
    print(numero,"*",i,"=",numero*i)
    # posso scriverlo anche
    # print(f"{numero} * {i} = {numero*i}")
    i = i+1

# esempio di ciclo for
frutti = ["banana", "mela", "pera"] #in python posso avere tipi diversi
for frutto in frutti:
    print(frutto)