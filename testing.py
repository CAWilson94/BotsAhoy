import requests 

HEADERS = {"Accept": "application/json", "User-Agent": "Yer Maw"}

r = requests.get("https://api.adviceslip.com/advice", headers=HEADERS)

print(r.json()['slip']['advice'])