from Bibita import Bibita

class Distributore:
    def __init__(self,capacita = 1, bevande = []):
        # capienza massima int numero di bevanda
        self.set_capacita(capacita)
        self.set_bevande(bevande)

    def set_capacita(self,capacita):
        if isinstance(capacita, int) and capacita > 0:
            self.__capacita = capacita
        else:
            self.__capacita = 1
    
    def get_capacita(self):
        return self.__capacita
    
    def set_bevande(self,bevande):
        if bevande != None and all(isinstance(x, Bibita) for x in bevande):
            pass
            self.__bevande = bevande
        else:
            self.__bevande = []

    def get_bevande(self):
        return self.__bevande
    
    def __str__(self):
        risposta = f"capacita':{self.__capacita}\n"

        i = 1
        for bibita in self.__bevande:
            risposta = risposta + str(i) + " {\n" + str(bibita) + "\n}\n"
            i = i + 1

        return risposta

    # add bevanda (bevanda) -> bool
    def add_bevanda (self, bibita):
        if isinstance(bibita, Bibita) and len(self.__bevande)<self.__capacita:
            self.__bevande.append(bibita)
            return True
        else:
            return False
    
    # somma totale bevande -> n bevande
    def somma_totale_bevande(self):
        '''
        i = 0
        for bevanda in self.__bevande:
            i = i + 1
        return i
        '''
        return len(self.__bevande) # meglio in questo modo che il ciclo
    
    # valore totale bevande -> float
    def valore_totale_bevande(self):
        i = 0.0
        for bevanda in self.__bevande:
            i = i + bevanda.get_prezzo()
        return i

    # eroga bevanda (bevanda, moneta_inserita) -> ritorna bevanda / None
    def eroga_bevanda(self,bevanda,moneta_inserita) -> Bibita: 
        # il -> va a specificare il tipo di return
        if not isinstance(bevanda, Bibita) or moneta_inserita<=0.0 or len(self.__bevande) == 0:
            return None
        
        # in python puoi scrivere "if bibita in self._bevande" e da vero se nel array c'è l'elemento
        for bibita in self.__bevande:
            if bibita.confronto_tra_bibite(bevanda) and moneta_inserita >= bibita.get_prezzo():
                self.__bevande.remove(bibita)
                return bibita
        return None