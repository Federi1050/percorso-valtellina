class Bibita:
    def __init__(self, nome = "ignoto", prezzo = 1.0, is_caffeinated = False):
        pass
        self.set_nome(nome)
        self.set_prezzo(prezzo)
        self.set_is_caffeinated(is_caffeinated)


    def set_nome(self,nome):
        if isinstance(nome, str) and len(nome)>0:
            self.__nome = nome
        else:
            self.__nome = "ignoto"

    def get_nome(self): 
        return self.__nome
    
    def set_prezzo(self,prezzo):
        if isinstance(prezzo, float) and prezzo > 0:
            self.__prezzo = prezzo
        else:
            self.__prezzo = 1.0

    def get_prezzo(self):
        return self.__prezzo
    
    def set_is_caffeinated(self,is_caffeinated):
        if isinstance(is_caffeinated, bool):
            self.__is_caffeinated = is_caffeinated
        else:
            self.__is_caffeinated = False

    def get_is_caffeinated(self):
        return self.__is_caffeinated
    
    def __str__(self):
        return f"nome:{self.__nome} , prezzo:{self.__prezzo} , caffeinato:{self.__is_caffeinated}"
    
    def confronto_tra_bibite(self, bibita):
        if not isinstance(bibita, Bibita):
            return False
        if self.__nome == bibita.get_nome() and self.__prezzo == bibita.get_prezzo() and self.__is_caffeinated == bibita.get_is_caffeinated():
            return True
        return False