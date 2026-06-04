# quando fai richiesta metti degli heder per fargli capire che sono un web browser
import requests
from bs4 import BeautifulSoup

url = "https://www.immobiliare.it/vendita-case/bergamo/"
headers = {"User-Agent": "Mozilla/5.0"}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

print(r.text)

#killmenow <3
