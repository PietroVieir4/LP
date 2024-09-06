'''Vinicius Pietro V. Rafael A.'''

lista1=[]
lista2=[]
lista3=[]

for i in range (2):
    user1=int(input(f"insira o {i+1}° numero"))
    lista1.append(user1)
    for j in range (2):
        user2=int(input(f"insira o {j+1}° numero"))
        lista2.append(user2)
        for f in range (2):
            user3=int(input(f"insira o {f+1}° numero"))
            lista3.append(user3)

matriz=[lista1, lista2, lista3]

print(matriz)