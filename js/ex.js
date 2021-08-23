"use strict";

const ps = require("prompt-sync")
const prompt = ps();

var vetorA = [5,2,3,1];
var vetorB = [1,2,3,4,5];

/*for(var i=0; i<5; i++){ 
    var inputA = parseInt(prompt(`Coloque aqui o elemento ${i} A: `));
    vetorA.push(inputA);
    var inputB = parseInt(prompt(`Coloque aqui o elemento ${i} B: `));
    vetorB.push(inputB);
}*/

console.log(vetorA);
console.log(vetorB);
console.log(vetorB.length);

/*for (var j=0; j<vetorB.length; j++){ 
    if(vetorA[j] == vetorB[j]){ 
        console.log(`O Valor do elemento A é igual a: ${vetorA[j]} e o valor do elemento B é igual a: ${vetorB[j]}`);
    }
}*/

for(var i=0; i<vetorB.length; i++){
    for(var j=0; j<vetorA.length; j++){
        if(vetorA[i] === vetorB[j]){
            console.log(`O Valor do elemento A é igual a: ${vetorA[j]} e o valor do elemento B é igual a: ${vetorB[j]}`);
        }
    }
}
