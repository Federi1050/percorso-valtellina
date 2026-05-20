import requests

url = "https://randomfox.ca/floof"

resp = requests.get(url, timeout=10)

if resp.status_code == 200:
    data = resp.json()

    image = data.get("image")
    link = data.get("link")

    print(f"image : {image} \n link : {link}")
    
else:
    print(f"Errore: status code {resp.status_code}")