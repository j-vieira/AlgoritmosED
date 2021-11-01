print("ELEIÇÃO DO NUNCA")
print("----------------------------------------------------------------")

numeroVotosCapitaoGancho = int(input("Insira a quantidade de votos do Capitao Gancho: "))
numeroVotosPeterPan = int(input("Insira a quantidade de votos do Peter Pan: "))
numeroVotosWendy = int(input("Insira a quantidade de votos da Wendy: "))
numeroVotosTotal = numeroVotosCapitaoGancho + numeroVotosPeterPan + numeroVotosWendy
metadeVotosTotal = numeroVotosTotal/2

if(numeroVotosCapitaoGancho > metadeVotosTotal or numeroVotosPeterPan > metadeVotosTotal or numeroVotosWendy > metadeVotosTotal):
    if(numeroVotosCapitaoGancho>metadeVotosTotal):
        print("Capitao Gancho ganhou a eleicao.")
    elif(numeroVotosPeterPan > metadeVotosTotal):
        print("Peter Pan ganhou a eleicao.")
    else: 
        print("Wendy ganhou a eleicao.")
else: #se ninguem ganhou no primeiro turno, vamos ao segundo
    print("----------------------------------------------------------------\n")
    print("SEGUNDO TURNO")
    
    numeroVotosCapitaoGancho = int(input("Insira a quantidade de votos do Capitao Gancho: "))
    numeroVotosPeterPan = int(input("Insira a quantidade de votos do Peter Pan: "))
    numeroVotosWendy = int(input("Insira a quantidade de votos da Wendy: "))

    if(numeroVotosCapitaoGancho>numeroVotosPeterPan and numeroVotosCapitaoGancho>numeroVotosWendy):
        print("Capitao Gancho ganhou a eleicao.")
    elif(numeroVotosPeterPan>numeroVotosCapitaoGancho and numeroVotosPeterPan>numeroVotosWendy):
        print("Peter Pan ganhou a eleicao.")
    else:
        print("Wendy ganhou a eleicao.")
