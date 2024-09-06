'''
Vinicius, Pietro V e Rafael A
Exercicio 3
'''

lista1=[]
lista2=[]
lista3=[]

for i in range (3):
    user1=int(input(f"insira o {i+1}° numero\n"))
    lista1.append(user1)
for j in range (3):
    user2=int(input(f"insira o {j+4}° numero\n"))
    lista2.append(user2)
for f in range (3):
    user3=int(input(f"insira o {f+7}° numero\n"))
    lista3.append(user3)

matriz=[lista1, lista2, lista3]


for colunas in matriz:
    for elemento in colunas:
        if elemento %2 == 0:
            print (elemento)
    


