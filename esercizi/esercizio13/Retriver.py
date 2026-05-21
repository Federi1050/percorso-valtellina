import requests

class Retriver:
    def __init__(self):
        pass
        self.__url = "https://rock-paper-scissors14.p.rapidapi.com/"

    def mossa_avversario(self, mossa_u):

        if self.controllo_mossa_valida(mossa_u):

            mossa_u = {"choice":mossa_u}

            headers = {
	            "x-rapidapi-key": "445fc05fbfmsh1c0f901465c258dp1fd045jsnb068cb869995",
	            "x-rapidapi-host": "rock-paper-scissors14.p.rapidapi.com",
	            "Content-Type": "application/json"
            }

            response = requests.get(self.__url, headers=headers, params=mossa_u)
        
        else:
            return "Mossa non valida"
        
        if response.status_code == 200:
            return response
        else:
            return f"Errore request codice: {response.status_code}"
        
    def controllo_mossa_valida(self,mossa):
        if mossa != "rock" and mossa != "paper" and mossa != "scissor":
            return False
        return True