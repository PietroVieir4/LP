'''
Vinicius, Pietro V e Rafael A
Exercicio 5
'''

lista1=[]
lista2=[]
lista3=[]

for i in range (3):
    user1=int(input(f"insira o {i+1}° numero"))
    lista1.append(user1)
for j in range (3):
    user2=int(input(f"insira o {j+4}° numero"))
    lista2.append(user2)
for f in range (3):
    user3=int(input(f"insira o {f+7}° numero"))
    lista3.append(user3)

matriz=[lista1, lista2, lista3]

def produto_matriz(matriz):
    produto_total = 1
    for linha in matriz:
        for item in linha:
            produto_total *= item
    return produto_total



resultado = produto_matriz(matriz)
print(f"O produto de todos os itens da matriz é: {resultado}")

