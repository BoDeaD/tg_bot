import json
import requests
from bs4 import BeautifulSoup as bs

URL_TEMPLATE = "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/"

response = requests.get(URL_TEMPLATE)

soup = bs(response.text, "html.parser")

all_tariffs = soup.find("div", clas = "MuiGrid-root MuiGrid-container css-2z6xcl")

print(all_tariffs)