from Meal_retriver import Meal_reatriver
from Ricetta import Ricetta

nome = str(input("inserisci il nome del piatto che vuoi cercare "))
meal_reatriver = Meal_reatriver("https://www.themealdb.com/api/json/v1/1/search.php?s=", 
                                "https://www.themealdb.com/api/json/v1/1/random.php")

risposta = meal_reatriver.get_meal_by_name(nome)

if isinstance(risposta, int):

    print(f"errore nella richiesta, codice errore: {risposta}")

else:
        
    ricetta = Ricetta(risposta)
    print("Ricerca per nome")
    print(ricetta)

risposta = meal_reatriver.get_meal_random()

if isinstance(risposta, int):

    print(f"errore nella richiesta, codice errore: {risposta}")

else:
        
    ricetta = Ricetta(risposta)
    print("Ricerca random")
    print(ricetta)