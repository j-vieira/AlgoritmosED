numeroM = int(input("Coloque o numero m: "))
numeroN = int(input("Coloque o numero n: "))

if(numeroM>numeroN):
    lado1 = numeroM**2-numeroN**2
    lado2 = 2*numeroM*numeroN 
    hipotenusa = numeroM**2+numeroN**2
    print("A tripla pitagorica eh a seguinte: ", lado1, lado2, hipotenusa)
else: print("O numero M deve ser maior do que o numero N, se nao o codigo nao funciona.")


