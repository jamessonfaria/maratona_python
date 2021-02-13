from day_06.indeed import scrapping_indeed

res_python = scrapping_indeed("https://br.indeed.com/empregos-de-python")
res_js = scrapping_indeed("https://br.indeed.com/empregos-de-javascript")

print(res_python)
print(res_js)

  
