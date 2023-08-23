let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
let sum = 0;
input.map((e) => {
  sum += Number(e);
});
console.log(sum);
