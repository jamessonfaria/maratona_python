from day_07.indeed import search_keyword 
from day_07.stackoverflow import scrapping_so
from day_07.save import save_to_csv


#result = search_keyword("python")
#result = scrapping_indeed(["https://br.indeed.com/empregos-de-python"])
#save_to_csv(result)

result = scrapping_so(["https://stackoverflow.com/jobs?q=python&pg=2"])
save_to_csv(result)

  
