numero1 = int(input("Coloque o primeiro numero: "))
numero2 = int(input("Coloque o segundo numero: "))
operacao = str(input("Coloque a operacao desejada: "))

def soma(numero1, numero2):
    return print(numero1+numero2)

def subtracao(numero1, numero2):
    return print(numero1-numero2)

def multiplicacao(numero1,numero2):
    return print(numero1*numero2)

def divisao(numero1, numero2):
    return print(numero1/numero2)

if operacao == "soma":
    soma(numero1, numero2)
if operacao == "subtracao":
    subtracao(numero1, numero2)
if operacao == "multiplicacao":
    multiplicacao(numero1, numero2)
if operacao == "divisao":
    divisao(numero1, numero2)
