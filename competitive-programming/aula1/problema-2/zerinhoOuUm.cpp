#include <bits/stdc++.h>

using namespace std;
// 1 0 0 
int main(){
    int tentativas;
    cin >> tentativas;
    while(tentativas){
        int a, b, c;

        cin >> a;
        cin >> b;
        cin >> c; 

        vector<int> zerinhoUm = {a,b,c};

        int qtdZero = 0; int qtdUm = 0; 
        int posZero =  0; int posUm = 0;

        for(int i=0; i<zerinhoUm.size(); i++){
            if(zerinhoUm[i] == 0){
                qtdZero++;
                posZero = i;
            }
            else{
                qtdUm++;
                posUm = i;
            }
        }

        bool zeroVenceu, umVenceu, empate = false;

        if(qtdUm == 3 || qtdZero == 3)
            cout << "0" << endl;
        else if(qtdUm < qtdZero)
            cout << posUm+1 << endl;
        else if(qtdZero < qtdUm)
            cout << posZero+1 << endl;
    
        tentativas--;
    }
}