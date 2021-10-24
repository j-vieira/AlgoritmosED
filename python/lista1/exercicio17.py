baseRetangulo = int(input("Coloque a base do retangulo: "))
alturaRetangulo = int(input("Coloque a altura do retangulo: "))

areaRetangulo = baseRetangulo*alturaRetangulo
perimetro = baseRetangulo*2+alturaRetangulo*2
diagonal = (baseRetangulo**2+alturaRetangulo**2)**(1/2)

print("A area é: ", areaRetangulo)
print("O perimetro é: ", perimetro)
print("A diagonal é: ", diagonal)
