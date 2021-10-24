salarioJoao = int(input("Coloque aqui o salario do Joao: "))
quantidadeContas = int(input("Coloque quantas contas Joao tera que pagar: "))
contas = []     
somaContas = 0

for i in range(quantidadeContas):
    valorConta = float(input("Coloque o valor da conta " + str(i+1) + ": "))
    valorConta = valorConta+valorConta*0.02
    contas.append(valorConta)
    somaContas = somaContas + valorConta

restante = salarioJoao - somaContas

print(restante)
