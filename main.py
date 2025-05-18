import requests
from bs4 import BeautifulSoup
import json

def get_news():
  url = "https://www.uol.com.br"
  response = requests.get(url)

  noticias = []
  
  soup = BeautifulSoup(response.text, "html.parser")
  tags = soup.find_all('h3')[:10]

  for tag in tags:
    titulo = tag.text.strip()
    noticias.append({ "titulo": titulo })
  return noticias

def save_json(noticias):
  with open("data/noticias.json", "w", encoding="utf-8") as arquivo:
    json.dump(noticias, arquivo)

noticias = get_news()
save_json(noticias)
print("Arquivo noticias.json gerado com sucesso!")
