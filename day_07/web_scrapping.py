from day_07.indeed import search_indeed_keyword 
from day_07.stackoverflow import search_so_keyword
from day_07.save import save_to_csv


#result = search_keyword("python")
#result = scrapping_indeed(["https://br.indeed.com/empregos-de-python"])
#save_to_csv(result)

#result = scrapping_so(["https://stackoverflow.com/jobs?q=python&pg=2"])

search = 'python'
result_indeed = search_indeed_keyword(search)
result_so = search_so_keyword(search)

all_results = result_indeed + result_so
save_to_csv(all_results)

  
