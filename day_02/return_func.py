def p_plus(n1, n2):
  print(n1+n2)

def r_plus(n1, n2):
  return n1 + n2

p_result = p_plus(10, 20)  
r_result = r_plus(10, 20)

print(p_result, r_result)

print(r_result + 50)


def welcome(name, email, id):
  msg = f"Olá {name}, seu email é {email} e seu id é {id}"
  return msg

print(welcome(id=133, name="james", email="jj@aol.com"))