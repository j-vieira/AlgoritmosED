numeroString = str(input("Insira um numero de 4 digitos: "))
if len(numeroString)!=4:
    print("O numero não tem 4 digitos.")
else:
    numeroInt = int(numeroString)
    primeiroNumero = int(numeroString[0] + numeroString[1])
    segundoNumero = int(numeroString[2] + numeroString[3])

    somaAoQuadrado = (primeiroNumero + segundoNumero)**2

    if(somaAoQuadrado==numeroInt):
        print("Os numeros são iguais.")
    else:
        print("Os numeros são diferentes.")