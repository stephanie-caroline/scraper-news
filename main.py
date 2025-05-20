import requests
from bs4 import BeautifulSoup
import json

def fetch_html():
  url = "https://noticias.uol.com.br/"
  response = requests.get(url)
  return response.text

def extract(data):
  soup = BeautifulSoup(data, "html.parser")
  tags = soup.find_all('h3')[:10]

  data_list = []

  for tag in tags:
    title = tag.text.strip()
    data_list.append({ "title": title })
  return data_list

def save_data_json(data, filepath="./data/noticias.json"):
  with open(filepath, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

def main():
  html = fetch_html()
  news_list = extract(html)
  save_data_json(news_list)

main()
