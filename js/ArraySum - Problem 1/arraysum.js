"use strict";

const ps = require("prompt-sync")
const prompt = ps();

var tamanhoDoArray = parseInt(prompt("Coloque o tamanho do array: "));
var array = [];
var soma = 0;

for(var i=0; i<tamanhoDoArray; i++) {
    var input = parseInt(prompt("Coloque o número desejado: "));
    array.push(input);
}

console.log(array);

for(var i=0; i<tamanhoDoArray; i++) {
    var soma = soma + array[i];
}

console.log(`A soma dos elementos é igual a ${soma}`);