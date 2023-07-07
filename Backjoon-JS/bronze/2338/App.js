let input = require('fs')
    .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
    .split('\n');
let A = BigInt(input[0]);
let B = BigInt(input[1]);
let sum = A + B;
let minus = A - B;
let multi = A * B;
console.log(sum.toString());
console.log(minus.toString());
console.log(multi.toString());
