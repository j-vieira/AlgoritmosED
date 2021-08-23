/* Alice e Bob criaram problemas para o HackerRank. As notas dos 
problemas criados são dadas de 1 a 100 considerando três categorias:
clareza, originalidade e dificuldade.

Notas de Alice: a[0], a[1], a[2], a[3].
Notas de Bob: b[0], b[1], b[2], b[3]. 

Temos que comparar a[i] com b[i] e se 
a[i]>b[i] -> Alice ganha 1 ponto;
a[i]=b[i] -> Ninguem ganha ponto;
a[i]<b[i] -> Bob ganha um ponto.
*/


const ps = require("prompt-sync")
const prompt = ps();

var pontosDaAlice = [];
var pontosDoBob = [];
var pontuacaoDoBob = 0; 
var pontuacaoDaAlice = 0;

for(var i=0; i<3; i++) {
    var pontoBob = prompt("Coloque aqui os pontos do Bob: ");
    var pontoAlice = prompt("Coloque aqui os pontos da Alice: ");

    if ((pontosDoBob[i] <= 100 && pontosDaAlice[i] <= 100)){
        
        pontosDaAlice.push(pontoAlice);
        pontosDoBob.push(pontoBob);

        if (pontosDoBob[i] > pontosDaAlice[i]) {
            console.log(`O ponto do Bob ${pontosDoBob[i]} é maior do que os ponto da Alice ${pontosDaAlice[i]}`);
            console.log("")
            pontuacaoDoBob++;
        }

        else if (pontosDaAlice[i] > pontosDoBob[i]) {
            console.log(`O ponto da Alice ${pontosDaAlice[i]} é maior do que os ponto do Bob ${pontosDoBob[i]}`);
            console.log("");
            pontuacaoDaAlice++;
        }

        else if (pontosDaAlice[i] = pontosDoBob[i]){
            console.log(`Os pontos ${pontosDaAlice[i]} / ${pontosDoBob[i]} são iguais`);
        }
    }
    else{
        console.log("Não é possivel colocar um valor maior do que 100")
    }
}

console.log(`Esses são os pontos de Bob: ${pontosDoBob}`);
console.log(`Esses são os pontos da Alice: ${pontosDaAlice}`);
console.log('-')
console.log(`Essa é a pontuação de Bob: ${pontuacaoDoBob}`);
console.log(`Essa é a pontuação da Alice: ${pontuacaoDaAlice}`);

if(pontuacaoDaAlice>pontuacaoDoBob){
    console.log("Alice ganhou");
}else{
    console.log("Bob ganhou");
}