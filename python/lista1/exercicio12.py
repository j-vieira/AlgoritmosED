numeroMoedas1Real = int(input("Coloque o numero de moedas de 1 real: "))
numeroMoedas50Centavos = int(input("Coloque o numero de moedas de 50 centavos: "))
numeroMoedas25Centavos = int(input("Coloque o numero de moedas de 25 centavos: "))
numeroMoedas10Centavos = int(input("Coloque o numero de moedas de 10 centavos: "))
numeroDeMoedas5Centavos = int(input("Coloque o numero de moedas de 5 centavos: "))
numeroDeMoedas1Centavo = int(input("Coloque o numero de moedas de 1 centavo: "))

quantidadeTotal = numeroMoedas1Real + numeroMoedas50Centavos*0.5 + numeroMoedas25Centavos*0.25 + numeroMoedas10Centavos*0.1 + numeroDeMoedas5Centavos*0.05 + numeroDeMoedas1Centavo*0.01
print(quantidadeTotal)