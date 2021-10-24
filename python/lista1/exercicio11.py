print("Equacao de Segundo Grau")
print("-----------------------")
a = int(input("Coloque o coeficiente a: "))
b = int(input("Coloque o coeficiente b: "))
c = int(input("Coloque o coeficiente c: "))

delta = (b**2)-(4*a*c)
raizDeDelta = delta**(1/2)

resultadoEquacao1 = (-b+raizDeDelta)/(2*a)
resultadoEquacao2 = (-b-raizDeDelta)/(2*a)

print("As raizes da equacao sao: " + str(resultadoEquacao1) + " " + str(resultadoEquacao2))
