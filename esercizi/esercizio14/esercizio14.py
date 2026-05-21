import math

def saluta(nome):
    print(f"Benvenuto {nome}")

def somma(a,b):
    return a+b

def massimo(a,b):
    if a > b:
        return a
    else :
        return b
    
    # return max([a,b])
    
def pai_o_dispari(numero):
    if numero%2 == 0:
        return "Pari"
    else:
        return "Dispari"
    
def area_reattangolo(base,altezza):
    return base*altezza

def celsius_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def conta_lettere(parola):
    return len(parola)

def quadrato(numero):
    return numero*numero

def media(a,b,c):
    return (a+b+c)/3

def inverti_stringa(testo):
    x = len(testo) - 1
    ris = ""
    while(x>=0):
        ris = ris + testo[x]
        x = x - 1
    return ris

def fattoriale(n):
    ris = 1
    for i in range(1,n+1):
        ris = ris * i
    return ris

def conta_vocali(testo):
    con = 0
    for i in range(len(testo)):
        if testo[i] == 'a' or testo[i] == 'e' or testo[i] == 'i' or testo[i] == 'o' or testo[i] == 'u':
            con = con + 1
    return con

def numero_primo(n):
    if n == 1: return False
    if n == 2: return False
    if n%2 == 0: return False
    for i in range(3, n, 2):
        if n%i == 0: return False
    return True

def somma_lista(lista):
    somma = 0
    for elemento in lista:
        somma = somma + elemento
    return somma

def massimo_lista(lista):
    return max(lista)

def minimo_lista(lista):
    return min(lista)

def palindroma(parola):
    start = 0
    base = len(parola)-1
    finish = base
    for i in range(int(len(parola)/2)):
        if parola[start] != parola[finish]: return False
        start = i
        finish = base - i
    return True

def moltiplica_lista(lista):
    ris = 1
    for i in lista:
        ris = ris * i
    return ris

def conta_pari(lista):
    ris = 0
    for i in lista:
        if i%2 == 0: ris = ris+1
    return ris

def tabellina(numero):
    for i in range(1,10):
        print(i*numero)

def fibonacci(n):
    lista = [1,2]
    for i in range(2,n+1):
        lista.append(lista[i-1]+lista[i-2])
    return lista[n-1]