class Ricetta:
    def __init__(self, json):
        pass
        self.codice = json.get("idMeal")
        self.nome = json.get("strMeal")
        self.country = json.get("strCountry")
        self.istruzioni = json.get("strInstruction")
        self.image = json.get("strMealThumb")
        self.video = json.get("strYoutube")

    def __str__(self):
        pass
        return (
            f"idMeal: {self.codice},\n"
            f"nomeMeal: {self.nome},\n"
            f"paese d'origine: {self.country},\n"
            f"istruzioni: {self.istruzioni},\n"
            f"immagine: {self.image},\n"
            f"video: {self.video}"
        )