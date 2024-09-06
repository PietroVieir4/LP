'''Vinicius Pietro V. Rafael A.'''

lista1=[]
lista2=[]
lista3=[]

matriz=[lista1, lista2, lista3]

for coluna in matriz:
    for elemento in coluna:
        for i in range (3):
            user1=int(input(f"insira o {i+1}° numero"))
            lista1.append(user1)
            if elemento<0:
                print(f"o {i+1} é negativo")
        for j in range (3):
            user2=int(input(f"insira o {j+1}° numero"))
            lista2.append(user2)
            if elemento<0:
                print(f"o {j+1} é negativo")
        for f in range (3):
            user3=int(input(f"insira o {f+1}° numero"))
            lista3.append(user3)
            if elemento<0:
                print(f"o {i+1} é negativo")

