import random
n = random.randint(1, 100)
lista = []

for i in range(0, n):
    x = random.randint(0,100)
    lista.append(x)

for i in range(0, n):
    if(lista[i]%2==0):
        print("par")
    else:
        print("impar")