import requests
from bs4 import BeautifulSoup

def scrapping_indeed(url):
  # url + request
  response = requests.get(url)
  # salva o html de retorno
  html_response = response.text
  # faz a sopa
  soup = BeautifulSoup(html_response, 'html.parser')
  # filtrar os cards
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
  return jobs

url_indeed = "https://br.indeed.com/empregos-de-python"
print(scrapping_indeed(url_indeed))
  
