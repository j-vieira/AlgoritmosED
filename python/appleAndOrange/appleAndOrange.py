#distancia casa do sam
s = 7
t = 10

#posicao arvore de maca
a = 4
#posicao arvore de laranja
b = 12

#tamanho do array macas (quantas macas tem)
m = 3
#tamanho do array laranja (quantas laranjas tem)
n = 3 

apples = [2,3,-4]
oranges = [3,-2,-4]
landApples = []
landOranges = []

for i in range(0, len(apples)):
    sumApples = a + apples[i]
    landApples.append(sumApples)
    if(landApples[i] >= s and landApples[i] <= t):
        print("A maca na distancia " + str(landApples[i]) + " caiu dentro do intervalo")

for j in range(0, len(oranges)):
    sumOranges = b + oranges[j]
    landOranges.append(sumOranges)
    if(landOranges[j] >= s and landOranges[j] <= t):
        print("A laranja na distancia " + str(landOranges[j]) + " caiu dentro do intervalo")

print(landApples, landOranges)


