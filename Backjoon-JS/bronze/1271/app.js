let input = require('fs')
.readFileSync(__dirname + '/input.txt', {encoding: 'utf-8'})
.split('\n')[0].split(' ');
let n = BigInt(input[0]);
let m = BigInt(input[1]);
console.log(n / m + '');
console.log(n % m + '');