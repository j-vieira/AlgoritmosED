// achei que a sequencia fosse outra coisa
#include <bits/stdc++.h>

using namespace std;

int calcularSequenciaEspecial(int numero){
    if(numero == 1){
        return 1;
    }
    
    int qtdNumeros = 1;
    int fimIntervalo = 1;
    int i = 2;

    int numero1 = 1;
    int numero2 = 2;

    while(fimIntervalo < numero){
        fimIntervalo = fimIntervalo + 2*i;
        i++;
        qtdNumeros++;
        numero1++; 
        numero2++;
        cout << qtdNumeros << " " << fimIntervalo <<  " n1:" << numero1 << " n2:" << numero2 << endl;
    }
    return fimIntervalo;
}

int main(){
    int tentativas;
    cin >> tentativas;
    
    while(tentativas){
        int numero;
        cin >> numero;

        cout << calcularSequenciaEspecial(numero) << endl;
        //calcularSequenciaEspecial(numero);
        tentativas--;
    }
}