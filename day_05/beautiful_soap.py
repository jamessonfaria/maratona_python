import requests
from bs4 import BeautifulSoup

url_indeed = "https://br.indeed.com/empregos-de-python"
r = requests.get(url_indeed)
html_request = r.text

soup = BeautifulSoup(html_request, 'html.parser')
print(soup.title)
#links = soup.find_all('a')

#for link in links:
#    print(link.get('href'))

title = soup.find("jl_c73d90042b5b9261")
print(title)  

file1 = open("myfile.txt","w")   
# \n is placed to indicate EOL (End of Line) 
file1.write(str(r.text)) 
file1.close() 