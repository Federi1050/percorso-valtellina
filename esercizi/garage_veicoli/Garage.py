from Mezzo import Mezzo

class Garage:
    def __init__(self):
        pass
        self.__posti_max = 15
        self.__mezzi_nel_garage = []

    def immissione(self,mezzo):
        if isinstance(mezzo, Mezzo) and len(self.__mezzi_nel_garage) < self.__posti_max and mezzo not in self.__mezzi_nel_garage:
            self.__mezzi_nel_garage.append(mezzo)
            return (len(self.__mezzi_nel_garage) - 1)
        else:
            print("non ci sta o gia' presente")
            return -1
        
    def estrazione(self,intero):
        if isinstance(intero, int) and intero >= 0 and intero < len(self.__mezzi_nel_garage):
            return self.__mezzi_nel_garage.pop(intero)
        else:
            return None
        
    def __str__(self):
        ris =  f"ELENCO MEZZI:\n"
        for mezzo in self.__mezzi_nel_garage:
                ris = ris + f"{str(mezzo)}\n"
        ris = ris.strip()
        return ris