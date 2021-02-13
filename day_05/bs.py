import requests
from bs4 import BeautifulSoup

url_indeed = "https://br.indeed.com/empregos-de-python"
r = requests.get(url_indeed)
html_request = r.text

soup = BeautifulSoup(html_request, 'html.parser')

cards = soup.find_all('div', class_="result")

jobs = []

for card in cards:
  job = {
    'title': card.find('a').get('title'),
    'company': card.find('span', class_='company').get_text(),
    'location': card.find('span', class_='location').string,
    'how_old': card.find('span', class_='date').string,
    'link': f"https://br.indeed.com{card.find('a').get('href')}"
  }
  jobs.append(job)

  print(jobs)
  
