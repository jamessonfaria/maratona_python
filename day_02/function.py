def welcome(name):
  msg = "Olá " + name
  print(msg)

aluno = "james"
welcome(aluno)

def plus(n1=0, n2=0):
  print(int(n1) + int(n2))

def minus(n1=0, n2=0):
  print(int(n1) - int(n2))

n1 = input("Digite o N1")
n2 = input("Digite o N2")
plus(n1, n2)
minus(n1, n2)

plus(10)

def interpolacao(name):
  print(f"Olá usuario: {name}")

interpolacao("Carlos")