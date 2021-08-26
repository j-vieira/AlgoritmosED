'''
 1 vela pra cada ano de idade
 Só se pode apagar as velas mais altas. Quantas velas são altas?

 velas = [4,4,1,3]
 O valor maximo é 4, então teremos 2 velas apagadas
'''

maiorVela = 0
velasApagadas = 1
velas.sort()

for i in range(0, len(velas)):
    if(velas[i] > velas[i-1]):
        maiorVela = velas[i]
        velasApagadas = 1
    if(velas[i] == velas[i-1]):
        velasApagadas += 1


print("A maior vela é " + str(maiorVela))
print(velasApagadas)
