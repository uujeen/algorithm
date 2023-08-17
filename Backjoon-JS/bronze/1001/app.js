let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');

const [a, b] = input[0].split(' ');
console.log(typeof (a - b));
