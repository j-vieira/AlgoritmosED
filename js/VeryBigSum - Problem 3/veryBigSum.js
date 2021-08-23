/*Function Description

Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

aVeryBigSum has the following parameter(s):

int ar[n]: an array of integers.
Return

long: the sum of all array elements
Input Format

The first line of the input consists of an integer n.
The next line contains n space-separated integers contained in the array.

Output Format

Return the integer sum of the elements in the array.*/ 

"use strict";

const ps = require("prompt-sync")
const prompt = ps();

var n = 1;
var array = [];
var soma = 0;

var n = parseInt(prompt("Coloque o tamanho do array: "));

if(n<=10){
    for (var i = 0; i < n; i++) {
        var input = parseInt(prompt("Coloque o elemento desejado: "));
        if(input>=0 && input<=10**10){
            array.push(input);
        }
        soma = soma + array[i];
    }
    console.log(array);  
    console.log(soma);
}

for(var i=0; i<n; i++){
    var input = parseInt(prompt("Coloque o elemento desejado: "));
    array.push(input);
    aVeryBigSum(n,array);
}

function aVeryBigSum(n, array) {
    if (n <= 10) {
        for (var i = 0; i < n; i++) {
            var input = parseInt(prompt("Coloque o elemento desejado: "));
            if (input >= 0 && input <= 10 ** 10) {
                array.push(input);
            }
            soma = soma + array[i];
        }
        console.log(array);
        console.log(soma);
    }
}
