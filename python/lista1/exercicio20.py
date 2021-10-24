nota1 = float(input("Coloque aqui a primeira nota: "))
peso1 = int(input("Coloque o peso da primeira nota: "))

nota2 = float(input("Coloque aqui a segunda nota: "))
peso2 = int(input("Coloque o peso da segunda nota: "))

nota3 = float(input("Coloque aqui a terceira nota: "))
peso3 = int(input("Coloque o peso da terceira nota: "))

mediaPonderada = (nota1*peso1+nota2*peso2+nota3*peso3)/(peso1+peso2+peso3)

print(mediaPonderada)