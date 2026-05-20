from Mobile import Mobile

class Stanza:
    def __init__(self, tipo, lista):
        pass
        self.set_tipologia(tipo) #str
        self.set_lista_mobili(lista) #mobili

    def set_tipologia(self, tipo):
        if isinstance(tipo, str) and len(tipo)>0:
            self.__tipo = tipo
        else:
            self.__tipo = "non specificato"

    def get_tipologia(self):
        return self.__tipo

    def set_lista_mobili(self, lista):
        if lista != None and all(isinstance(x, Mobile) for x in lista):
            pass
            self.__lista_mobili = lista
        else:
            self.__lista_mobili = []

    def get_lista_mobili(self):
        return self.__lista_mobili
    
    def __str__(self):
        pass
        risposta = f"tipologia={self.__tipo}\nmobili all interno=\n"
        i = 1
        for mobile in self.__lista_mobili:
                risposta = risposta + str(i) + " {\n" + str(mobile) + "\n}\n"
                i = i+1
        return risposta
    
    def aggiungi_mobile(self,mobile):
        if isinstance(mobile, Mobile):
            self.__lista_mobili.append(mobile)
            return True
        return False

    def rimuovi_mobile(self,mobile):
        if isinstance(mobile, Mobile) and len(self.__lista_mobili) != 0:
            return self.__lista_mobili.remove(mobile)
        return None
