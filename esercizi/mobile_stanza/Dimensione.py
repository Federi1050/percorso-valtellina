class Dimensione:
    def __init__(self, alt = 1.0, lungh = 1.0, prof = 1.0):
        pass
        # tutti float 
        self.set_altezza(alt)
        self.set_lunghezza(lungh)
        self.set_profondita(prof)

    def set_altezza(self, numero):
        if isinstance(numero, float) and numero>0:
            self.__altezza = numero
        else:
            self.__altezza = 1.0

    def set_lunghezza(self, numero):
        if isinstance(numero, float) and numero>0:
            self.__lunghezza = numero
        else:
            self.__lunghezza = 1.0

    def set_profondita(self, numero):
        if isinstance(numero, float) and numero>0:
            self.__profondita = numero
        else:
            self.__profondita = 1.0

    def get_altezza(self):
        return self.__altezza
    
    def get_lunghezza(self):
        return self.__lunghezza
    
    def get_profondita(self):
        return self.__profondita
    
    def __str__(self):
        pass
        return (
            f"altezza {self.__altezza}, "
            f"lunghezza {self.__lunghezza}, "
            f"profondita  {self.__profondita}"
        )