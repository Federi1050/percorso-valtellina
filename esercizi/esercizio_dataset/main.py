# dato dataset utilizzi tutte le info quindi dati che non vanno bene
# -> correggerli.
# identifica outlier e correggerli

from dataframe_manager import DataFrameManager

df_manager = DataFrameManager()

def carica_dataset():
    df_manager.caricare_dataset()

def stampa_dataset():
    print(df_manager)

def informazioni_dataset():
    df_manager.informazioni_dataset()

def gestione_valori_strani():
    df_manager.gestione_valori_strani()


print("Iniziamo")
print()

print("carico dataset")
carica_dataset()
print()

print("stampa dataset")
stampa_dataset()
print()

print("info sullì dataset")
informazioni_dataset()
print()

print("gestione valori non consoni")
gestione_valori_strani()
print()

print("stampa dataset")
stampa_dataset()
print()