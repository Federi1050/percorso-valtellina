from Dimensione import Dimensione

class Mobile:
    def __init__(self, materiale, prezzo, dimensione):
        pass
        self.set_materiale(materiale) #str
        self.set_prezzo(prezzo) #float > 0
        self.set_dimensione(dimensione) #Dimensione

    def set_materiale(self, materiale):
        if isinstance(materiale, str) and len(materiale)>0:
            self.__materiale = materiale
        else:
            self.__materiale = "ignoto"

    def get_materiale(self):
        return self.__materiale
    
    def set_prezzo(self, prezzo):
        if isinstance(prezzo, float) and prezzo>0:
            self.__prezzo = prezzo
        else:
            self.__prezzo = 1.0

    def get_prezzo(self):
        return self.__prezzo
    
    def set_dimensione(self, dimensione):
        if isinstance(dimensione, Dimensione):
            self.__dimensione = dimensione
        else:
            self.__dimensione = Dimensione()

    def get_dimensione(self):
        return self.__dimensione
    
    def __str__(self):
        pass
        return (
            f"materiale : {self.__materiale}\n"
            f"prezzo : {self.__prezzo}\n"
            f"dimensione : {self.__dimensione}"
        )