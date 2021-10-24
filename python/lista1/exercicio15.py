quantidadeDias = int(input("Coloque a quantidade de dias: "))

quantidadeAnos = quantidadeDias//365
quantidadeDias = quantidadeDias%365
quantidadeMeses = quantidadeDias//30
quantidadeDias = quantidadeDias%30

print(quantidadeAnos, "anos", quantidadeMeses, "meses", quantidadeDias, "dias")