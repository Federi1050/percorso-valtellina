# link https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata

import requests

class MealRetriver:
  def __init__(self, url):
    #self.__url = url   # creato un attributo privato di tipo str
    self.set_url(url)

  def get_url(self):
    return self.__url

  def set_url(self, url):
    if len(url) != 0:
      self.__url = url

  def get_meal_by_name(self , name , timeout = 10):
    if len(name) == 0:
      return "devi inserire un nome" 

    search = self.__url + name

    resp = requests.get(search, timeout=timeout)

    if resp.status_code == 200:
      data = resp.json()

      #{"meals":null}


      if data.get("meals") is None:
        return "Piatto non disponibile"
      return data.get("meals")[0].get("strInstructions")  + "Fine istruzione"

 
    else:
      print(f"Errore: status code {resp.status_code}")


meal_retriver = MealRetriver("https://www.themealdb.com/api/json/v1/1/search.php?s=")

print(meal_retriver.get_meal_by_name("Arrabiata"))