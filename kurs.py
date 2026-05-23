import requests
from datetime import datetime

url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
response = requests.get(url)
data = response.json()

now = datetime.now().strftime("%Y-%m-%d %H:%M")

with open("kursy.txt", "a") as file:
    file.write(now + "\n")
    for item in data:
        file.write(item["ccy"] + " -> " + item["buy"] + " UAH\n")
    file.write("---\n")

print("Saved to kursy.txt")
