quantidadeAnos = int(input("Coloque a quantidade de anos: "))
quantidadeMeses = int(input("Coloque a quantidade de meses: "))
quantidadeDias = int(input("Coloque a quantidade de dias: "))

quantidadeDias = quantidadeDias + quantidadeMeses*30 + quantidadeAnos*365
print(quantidadeDias)
