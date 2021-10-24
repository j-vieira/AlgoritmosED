totalHoras = int(input("Coloque a quantidade de horas: "))
totalMinutos = int(input("Coloque a quantidade de minutos: "))
totalSegundos = int(input("Coloque a quantidade de segundos: "))

horasEmSegundos = totalHoras*60*60
minutosEmSegundos = totalMinutos*60

totalSegundos = totalSegundos + horasEmSegundos + minutosEmSegundos

print(totalSegundos)
