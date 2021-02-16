import csv

def save_to_csv(jobs):
  file = open('jobs.csv', 'w')
  writer = csv.writer(file)
  writer.writerow(['title', 'company', 'location', 'how_old', 'link'])
  
  for job in jobs:
    values = list(job.values())
    writer.writerow(values)

