def unlock_adult_movies(username, age):
  if age < 18:
    msg = f"{username} não pode assistir filmes adultos."
  else:
    msg = f"{username} pode assistir filmes adultos."

  return msg

print(unlock_adult_movies("lucas", 12)) 
print(unlock_adult_movies("jorge", 18)) 
print(unlock_adult_movies("marcos", 25)) 
