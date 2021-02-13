import requests
from bs4 import BeautifulSoup

url_base = 'https://br.indeed.com/empregos?'
results_per_page = 50

def search_keyword(keyword):
  #1. faz a busca e descobra quantas pg de resultado
  response = requests.get(f'{url_base}q={keyword}&limit=50&start=0')
  html_response = response.text
  soup = BeautifulSoup(html_response, 'html.parser')
  
  # descobrimos quantas paginas analisando o codigo
  pages_links = soup.find('ul', class_="pagination-list").find_all('li')
  
  #lista que armazena paginas
  number_of_pages = [0]
  for link in pages_links:
    n_page = link.get_text()
    number_of_pages.append(n_page)

  urls = []
  for n_page in number_of_pages[:-1]:
    url = f"{url_base}q={keyword}&limit={results_per_page}&start={results_per_page * int(n_page)}"
    urls.append(url)

  print(urls)

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