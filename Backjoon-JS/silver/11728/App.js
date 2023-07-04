let input = require('fs')
.readFileSync(__dirname + '/input.txt', {encoding: 'utf-8'})
.split('\n');
let arrayA = input[1].split(' ');
let arrayB = input[2].split(' ');
let arrayC = arrayA.concat(arrayB).sort((a, b) => a - b);
console.log(arrayC.join(' '));