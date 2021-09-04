ar = [1, 2, 1, 2, 1, 3, 2, 3, 2, 2]
ar.sort()
listaParesDeMeias = []
# ar = [1,1,1,2,2,2,3]
contarMeiasIguais = 0
meiasPares = 0

for i in range(0, len(ar)):
  if(ar[i] == ar[i-1]):
    print("meias iguais" + " " + str(ar[i]) + " " + str(ar[i-1]))
    contarMeiasIguais = contarMeiasIguais + 1
  if(ar[i] != ar[i-1] and contarMeiasIguais != 0):
    listaParesDeMeias.append(contarMeiasIguais)
    print("meias diferentes" + " " + str(ar[i]) + " " + str(ar[i-1]))
    contarMeiasIguais = 0

pares = [int(i/2) for i in listaParesDeMeias]

for i in range(0, len(pares)):
  if i>0:
    print(pares, pares[i], pares[i-1])
    numeroPar = pares[i] + pares[i-1]

print(numeroPar)

'''
test = [int(i/2) for i in listaParesDeMeias]
print(test)


for i in range(0, len(test)):
  print(meiasPares, test[i])
  meiasPares += meiasPares + test[i]
  print(meiasPares)
'''
