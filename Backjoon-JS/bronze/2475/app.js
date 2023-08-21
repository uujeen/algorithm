let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
const [a, b, c, d, e] = input[0].split(' ').map(Number);
const sum = a ** 2 + b ** 2 + c ** 2 + d ** 2 + e ** 2;
const ans = sum % 10;
console.log(ans);
