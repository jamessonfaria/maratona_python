import requests

url_indeed = "https://br.indeed.com/empregos-de-python"
r = requests.get(url_indeed)

print(r.text)
