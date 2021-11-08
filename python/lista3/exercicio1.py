idade = 0

quantidadeHomens, quantidadeMulheres, quantidadeIdadeMenor30 = 0,0,0

mediaSalarialMasculina, mediaSalarialFeminina, mediaSalarialIdadeMenor30 = 0,0,0

salarioMenor30, salarioMasculino, salarioFeminino, salarioAtualM, salarioAtualF = 0,0,0,0,0

while idade>=0:
    idade = int(input("Coloque aqui a idade: "))
    sexo = str(input("Insira o sexo, M ou F: "))

    if(idade<30 and idade>0):
        salarioAntigoMenor30 = salarioMenor30
        quantidadeIdadeMenor30 += 1
        if(sexo == "M" or sexo == "m"):
            salarioAntigoM = salarioAtualM
            salarioMasculino = int(input("Coloque aqui o salario do funcionario: "))
            salarioAtualM = salarioAntigoM + salarioMasculino
            print("Salario antigo M", salarioAntigoM, "salario atual M", salarioAtualM, "Salario Masculino", salarioMasculino)
            quantidadeHomens += 1
            mediaSalarialMasculina = salarioAtualM/quantidadeHomens

            salarioAtualMenor30 = salarioAntigoMenor30 + salarioAtualM
            mediaSalarialIdadeMenor30 = salarioAtualMenor30/quantidadeIdadeMenor30

        elif(sexo == "F" or sexo == "f"):
            salarioAntigoF = salarioAtualF
            salarioFeminino = int(input("Coloque aqui o salario da funcionaria:"))
            salarioAtualF = salarioAntigoF + salarioFeminino
            print("Salario antigo F", salarioAntigoF, "salario atual F", salarioAtualF, "salarioFeminino", salarioFeminino)
            
            quantidadeMulheres += 1
            mediaSalarialFeminina = salarioAtualF/quantidadeMulheres
            print(mediaSalarialFeminina)
            salarioAtualMenor30 = salarioAntigoMenor30 + salarioAtualF
            mediaSalarialIdadeMenor30 = salarioAtualMenor30/quantidadeIdadeMenor30
        
    elif(idade>=30):
        if(sexo == "M" or sexo  == "m"):
            salarioAntigoM = salarioAtualM
            salarioMasculino = int(input("Coloque aqui o salario do funcionario: "))
            salarioAtualM = salarioAntigoM + salarioMasculino

            quantidadeHomens += 1
            mediaSalarialMasculina = salarioAtualM/quantidadeHomens

        elif(sexo == "F" or sexo == "f"):
            salarioAntigoF = salarioFeminino
            salarioFeminino = int(input("Coloque aqui o salario da funcionaria: "))
            salarioAtualF = salarioAntigoF + salarioFeminino
    else:
        continue

print("A media salarial masculina é", mediaSalarialMasculina, "\nA media salarial feminina é", mediaSalarialFeminina)
print("A media salarial daqueles que tem menos de 30 anos eh:", mediaSalarialIdadeMenor30)