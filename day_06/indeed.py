import requests
from bs4 import BeautifulSoup

url_base = 'https://br.indeed.com/empregos?'
results_per_page = 50

def search_keyword(keyword):
  # url + request
  response = requests.get(f'{url_base}q={keyword}&limit=50&start=0')
  # salva o html de retorno
  html_response = response.text
  # faz a sopa
  soup = BeautifulSoup(html_response, 'html.parser')

  pages_links = soup.find('ul', class_="pagination-list").find_all('li')

  number_of_pages = []
  for link in pages_links:
    n_page = link.get_text()
    number_of_pages.append(n_page)

  print(number_of_pages[:-1])


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