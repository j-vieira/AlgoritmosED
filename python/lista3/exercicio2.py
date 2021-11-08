numerosDaPa = int(input("Insira o N primeiros termos da PA: "))
RAZAO = int(input("Razão da PA: "))
total = 0

for i in range(0, numerosDaPa):
    total = total + RAZAO

print(total)
