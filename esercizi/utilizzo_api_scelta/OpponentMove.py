# esempio json
#{"user":{"name":"rock","beats":"scissors"},"ai":{"name":"paper","beats":"rock"},"result":"You Lose"}

class GameState:
    def __init__(self,data):
        pass
        if isinstance(data, dict):
            self.__is_valido = True
            self.parsing(data)
        else:
            self.__is_valido = False
            self.__user = None
            self.__ai = None
            self.__result = None

    def parsing(self,data):
        self.set_us(data.get("user"))
        self.set_ai(data.get("ai"))
        self.set_result(data.get("result"))

    def set_us(self, string):
        self.__user = Mossa(string)
    
    def set_ai(self, string):
        self.__ai = Mossa(string)

    def set_result(self, string):
        self.__result = string

    def get_is_valido(self):
        return self.__is_valido

    def get_us(self):
        return self.__user
    
    def get_ai(self):
        return self.__ai
    
    def get_result(self):
        return self.__result

    def __str__(self):
        pass
        return (
            f"game valido : {str(self.__is_valido)}\n"
            f"mossa utente : {str(self.__user)}\n"
            f"mossa ai : {str(self.__ai)}\n"
            f"risultato : {str(self.__result)}\n"
        )

class Mossa:
    def __init__(self, data):
        pass
        self.set_name(data.get("name"))
        self.set_beat(data.get("beats"))

    def get_name(self):
        return self.__name

    def get_beat(self):
        return self.__beat

    def set_name(self, name):
        self.__name = name

    def set_beat(self, beat):
        self.__beat = beat

    # Metodo stringa
    def __str__(self):
        return f"Mossa(name={self.__name}, beat={self.__beat})"