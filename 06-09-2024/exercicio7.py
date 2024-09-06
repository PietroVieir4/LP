'''Vinicius Pietro V. Rafael A.'''

lista1 = []
lista2 = []
lista3 = []

for i in range(3):
    user1 = int(input(f"Insira o {i+1}° número para a primeira linha: "))
    lista1.append(user1)
for j in range(3):
    user2 = int(input(f"Insira o {j+1}° número para a segunda linha: "))
    lista2.append(user2)
for f in range(3):
    user3 = int(input(f"Insira o {f+1}° número para a terceira linha: "))
    lista3.append(user3)

matriz = [lista1, lista2, lista3]

if matriz==[[1, 0 ,0], [0, 1, 0], [0, 0, 1]]:
    print("é uma matriz identidade")
else:
    print("não é matriz identidade")