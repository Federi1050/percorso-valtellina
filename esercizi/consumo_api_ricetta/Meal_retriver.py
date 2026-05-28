# usando theMealDb
# cercare piatto per nome dato da utente
# fa la richiesta e stampa i risulati

import requests

class Meal_reatriver:

    def __init__ (self, urlNome, urlRandom):
        self.set_url_nome(urlNome)
        self.set_url_random(urlRandom)

    def set_url_nome(self, url):
        if len(url) != 0:
            self.__urlnome = url
    
    def get_url_nome(self):
        return self.__urlnome
    
    def set_url_random(self, url):
        if len(url) != 0:
            self.__urlrandom = url
    
    def get_url_random(self):
        return self.__urlrandom

    def get_meal_by_name(self,name):

        if len(name) == 0:
            print("il nome deve essere almeno 1 carattere")
            return -1
        
        url = self.__urlnome + name

        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get("meals") is None:
                print("nessun piatto trovato")
                return -2
            else:
                return data.get("meals")[0] 
        else:
            return resp.status_code
        
    def get_meal_random(self):
        
        url = self.__urlrandom

        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get("meals") is None:
                print("nessun piatto trovato")
                return -2
            else:
                return data.get("meals")[0] 
        else:
            return resp.status_code