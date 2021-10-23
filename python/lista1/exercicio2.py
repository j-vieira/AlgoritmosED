provaUm   = float(input("Coloque a nota da primeira prova: "))
provaDois = float(input("Coloque a nota da segunda prova: "))

trabalho  = float(input("Coloque a nota do trabalho: "))

lista1 = float(input("Coloque a nota da primeira lista: "))
lista2 = float(input("Coloque a nota da segunda lista: "))
lista3 = float(input("Coloque a nota da terceira lista: "))
lista4 = float(input("Coloque a nota da quarta lista: "))
lista5 = float(input("Coloque a nota da quinta lista: "))

mediaListas = (lista1+lista2+lista3+lista4+lista5)/5

media = 0.3*provaUm + 0.4*provaDois + 0.2*mediaListas + 0.1*trabalho

print(media)




