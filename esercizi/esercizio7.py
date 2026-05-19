class Telefono:
    def __init__(self, modello, marca, is_dual_sim, costo = 0): # costo ha un valore di default, se 
                                                                #non viene dato viene messo a quel valore
        self.set_modello(modello)
        self.set_costo(costo)
        self.set_marca(marca)
        self.set_dual_sim(is_dual_sim)

    def set_modello(self, modello):
        if isinstance(modello, str) and modello:
            self.__modello = modello
        else:
            print("il modello dovrebbe essere una stringa")
    
    def set_costo(self, costo):
        if isinstance(costo, int) and costo>0:
            self.__costo = costo
        else:
            print("errore nel settaggio del costo")
    
    def set_marca(self, marca):
        if isinstance(marca, str) and marca:
            self.__marca = marca
        else:
            print("la marca dovrebbe essere una stringa")

    def set_dual_sim(self, is_dual_sim):
        if isinstance(is_dual_sim, bool) and self.controllo_marca_sim(is_dual_sim):
            self.__is_dual_sim = is_dual_sim
        else:
            print("errore nel settaggio del dual sim boolean")

    def get_modello(self):
        return self.__modello

    def get_costo(self):
        return self.__costo

    def get_marca(self):
        return self.__marca

    def get_is_dual_sim(self):
        return self.__is_dual_sim
    
    def controllo_marca_sim(self, is_dual_sim):
        if self.__marca == "Apple" and is_dual_sim == True:
            return False
        else:
            return True
        
    def __str__(self): #potresti usare i getter ma conviene chiamare direttamente l'attributo
                       #ricorda che quando metti f convertirebbe i metodi getter in stringa e non li usa
        return (
            f"modello: {self.__marca} costo: {self.__costo} marca: {self.__marca} "
            f"dual sim: {self.__is_dual_sim}"
        )
        #questa scrittura così permette di spezzare la stringa solo qui

telefono1 = Telefono("A10","android",True,999)
print(telefono1)