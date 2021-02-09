### list
students = ["jame", "carlos", "amanda"]
numbers = [1, 10, 100]

print(students)
print(numbers)
print(students[1])
print(students[-1])

print(len(numbers))
numbers.append(1000)
print(numbers)
numbers.pop()
print(numbers)

students.remove("carlos")
print(students)

novo_aluno = "max"
students.insert(1, novo_aluno)
print(students)

numbers.reverse()
print(numbers)

print(type(numbers))