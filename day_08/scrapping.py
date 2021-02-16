from day_07.indeed import search_indeed_keyword 
from day_07.stackoverflow import search_so_keyword

def get_jobs(keyword):
  result_indeed = search_indeed_keyword(keyword)
  result_so = search_so_keyword(keyword)
  all_results = result_indeed + result_so
  return all_results