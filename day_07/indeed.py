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
  pages_links = soup.find('ul', class_="pagination-list").find_all('a')
  
  #lista que armazena paginas
  number_of_pages = [0,1]
  for link in pages_links:
    n_page = link.string
    if n_page == None:
      continue
    number_of_pages.append(int(n_page))

  urls = []
  for n_page in number_of_pages:
    url = f"{url_base}q={keyword}&limit={results_per_page}&start={results_per_page * n_page}"
    urls.append(url)

  return scrapping_indeed(urls)

def scrapping_indeed(urls):
  all_jobs = []
  for url in urls:
    print("começando uma url...")
    response = requests.get(url)
    html_response = response.text
    soup = BeautifulSoup(html_response, 'html.parser')
    # filtrar os cards
    cards = soup.find_all('div', class_="result")
    for card in cards:
      job = {
        'title': card.find('a').get('title'),
        #'company': card.find('span', class_='company').get_text(),
        'location': card.find('span', class_='location').string,
        'how_old': card.find('span', class_='date').string,
        'link': f"https://br.indeed.com{card.find('a').get('href')}"
      }
      all_jobs.append(job)
  return all_jobs