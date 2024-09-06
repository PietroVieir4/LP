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


print("\nMatriz 4x4 inserida:")
for linha in matriz:
    print(" ".join(map(str, linha)))


print("\nElementos da diagonal secundária:")
tamanho = len(matriz)

for i in range(tamanho):
    j = tamanho - 1 - i
    print(f"Elemento na posição ({i+1}, {j+1}): {matriz[i][j]}")
