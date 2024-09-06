'''Vinicius Pietro V. Rafael A.'''

lista1 = []
lista2 = []
lista3 = []
lista4 = []

for i in range(4):
    user1 = int(input(f"Insira o {i+1}° número para a primeira linha: "))
    lista1.append(user1)
for j in range(4):
    user2 = int(input(f"Insira o {j+1}° número para a segunda linha: "))
    lista2.append(user2)
for f in range(4):
    user3 = int(input(f"Insira o {f+1}° número para a terceira linha: "))
    lista3.append(user3)
for m in range(4):
    user4 = int(input(f"Insira o {m+1}° número para a quarta linha: "))
    lista4.append(user4)

matriz = [lista1, lista2, lista3, lista4]

maiorq10=0

for coluna in matriz:
    for elemento in coluna:
        if elemento>10:
            maiorq10+=1
print(f"essa matriz tem {maiorq10} elementos com valores maior do que 10")