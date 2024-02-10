#include <bits/stdc++.h>

using namespace std;

string rotacionarCuboVertical(string cubo){
    string novoCubo = cubo;

    novoCubo[0] = cubo[4];
    novoCubo[1] = cubo[0];
    novoCubo[4] = cubo[5];
    novoCubo[5] = cubo[1];

    return novoCubo;
}

string rotacionarCuboHorizontal(string cubo){
    // 2 4 5 3  vira 3 2 4 5
    // 1 3 4 2  vira 2 1 3 4
    string novoCubo = cubo;

    novoCubo[1] = cubo[2];
    novoCubo[3] = cubo[1];
    novoCubo[4] = cubo[3];
    novoCubo[2] = cubo[4];

    return novoCubo;
}

string verificarCubosIsomorfos(string primeiroCubo, string segundoCubo){
    bool cubosIsomorfos = false;
    string cuboRotacionado = primeiroCubo;
    string cuboRotacionadoVertical;
    
    if(primeiroCubo.size() != segundoCubo.size()){
        return "N";
    }

    for(int i=0; i<4; i++){
        if(cuboRotacionado.compare(segundoCubo) == 0){
            return "S";
        }
        cuboRotacionado = rotacionarCuboHorizontal(cuboRotacionado);
        for(int i=0; i<4; i++){
            if(cuboRotacionadoVertical.compare(segundoCubo) == 0){
                return "S";
            }
            cuboRotacionadoVertical = rotacionarCuboVertical(cuboRotacionado);
        }
    }
    return "N";
}

int main(){
    int tentativas;
    cin >> tentativas;
    while(tentativas){
        string primeiroCubo;
        string segundoCubo;

        cin >> primeiroCubo;
        cin >> segundoCubo;

        cout << verificarCubosIsomorfos(primeiroCubo, segundoCubo) << endl; 
        
        tentativas--;
    }
}