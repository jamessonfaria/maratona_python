students = [
    {"name": "bruno", "score": 50},
    {"name": "marcos", "score": 10},
    {"name": "gabriel", "score": 30},
    {"name": "sandro", "score": 20},
    {"name": "amanda", "score": 20},
    {"name": "luana", "score": 40},
    {"name": "thiago", "score": 55},
    {"name": "thereza", "score": 52},
    {"name": "cristina", "score": 11}
]

for student in students:
  score = student["score"]
  if score < 40:
    print(f"O aluno(a) {student['name']} reprovou")
  else:
    print(f"O aluno(a) {student['name']} aprovou")
  print("#########")


for i in students:
  if i["score"] <= 10:
    print("Um aluno reprovou")
    break
  else:
    print(i["name"])

for i in students:
  if i["score"] < 30:
    continue
  else:
    print(i["name"])