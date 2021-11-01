salarioVendedor = 2200
quantidadeEmpregadosNaLoja = int(input("Quantos funcionarios temos na loja?\n"))
valorVendasMes = float(input("Coloque aqui o valor das vendas do mes: "))
bonus = valorVendasMes * 0.05
print(bonus)
salarioTotal = salarioVendedor+(bonus/quantidadeEmpregadosNaLoja)

print("O salario total de cada empregado é de", salarioTotal)