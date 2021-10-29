print("Numeros ordenados de forma crescente")

numero1 = int(input("Coloque o primeiro numero: "))
numero2 = int(input("Coloque o segundo numero: "))
numero3 = int(input("Coloque o terceiro numero: "))

numeros = [numero1, numero2, numero3]

print("A lista de numeros inicialmente é:", numeros)

def ordenar(numeros):
    for i in range(1, len(numeros)):
        chave = numeros[i]
        k = i
        while k > 0 and chave < numeros[k-1]:
            numeros[k] = numeros[k-1]
            k = k-1
        numeros[k] = chave

ordenar(numeros)

print("Estes são os numeros de forma crescente:", numeros)
