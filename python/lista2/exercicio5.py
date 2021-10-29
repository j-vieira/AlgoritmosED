print("Calculadora de peso ideal, coloque o sexo como M ou F e terá o peso ideal.")

alturaPessoa = float(input("Altura da pessoa: "))
sexoPessoa = str(input("Insira o sexo da pessoa: "))

def pesoIdeal(alturaPessoa, sexoPessoa):
    if(sexoPessoa=="M"):
        pesoIdeal = (72.7*alturaPessoa) - 58.0
    else:
        pesoIdeal = (62.1*alturaPessoa) - 44.7 
    print(pesoIdeal)

pesoIdeal(alturaPessoa, sexoPessoa)