let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
let answer = '';
for (let i = parseInt(input[0]); i > 0; i--) {
  answer += i + '\n';
}
console.log(answer);
