let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
console.log(
  input[0]
    .split(' ')
    .sort((a, b) => a - b)
    .join(' ')
);
