import requests

url_indeed = "https://br.indeed.com/empregos-de-python"
r = requests.get(url_indeed)
if r.status_code == 200:
  print("o site esta online")
else:
  print("o site esta off")
