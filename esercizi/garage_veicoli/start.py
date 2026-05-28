from Mezzo import Mezzo
from Mezzo import Automobile
from Mezzo import Moto
from Mezzo import Furgone
from Garage import Garage

g = Garage()

a1 = Automobile(2020, "Fiat", "Diesel", 1600, 5)
a2 = Automobile(2022, "BMW", "Benzina", 2000, 3)
m1 = Moto(2021, "Yamaha", "Benzina", 900, "Sportiva", 4)
m2 = Moto(2019, "Honda", "Benzina", 750, "Turistica", 2)
m3 = Moto(2023, "Ducati", "Benzina", 1100, "Sportiva", 4)
f1 = Furgone(2018, "Iveco", "Diesel", 3000, 1500)

mezzi = [a1, a2, m1, m2, m3, f1]

print("=== INSERIMENTO MEZZI ===")
for mezzo in mezzi:
    print("inserito in posizione:", g.immissione(mezzo))


print("\n=== STATO GARAGE ===")
print(g)

print("\n=== ESTRAZIONE POSIZIONE 2 ===")
estratto = g.estrazione(2)
print("estratto:", estratto)

print("\n=== STATO DOPO ESTRAZIONE ===")
print(g)