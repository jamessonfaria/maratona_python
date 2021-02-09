### Dictonary

aluno = {
  "nome" : "jamesson",
  "idade" : 24,
  "brazil" : True,
  "fav_foods": ["Pizza", "Hot"]
}

print(aluno)
print(type(aluno))
print(aluno["nome"])
aluno["nome"] = "kai"
aluno["score"] = 100
print(aluno)
print(aluno.keys())
print(aluno.values())

alunos = [
  { 
    "nome" : "jamesson",
    "idade" : 24,
    "brazil" : True,
  },
  {
    "nome" : "amanda",
    "idade" : 22,
    "brazil" : True,
  },
  {
    "nome" : "peter",
    "idade" : 34,
    "brazil" : False,
  },
]

print(alunos)
print(alunos[0]["nome"])
print(alunos[1]["nome"])

for aluno in alunos:
  print(aluno["nome"])
  print(aluno["idade"])
  print("########")
  