let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
const max = Number(input[0].split(' '));
let ans = '';
for (let i = 1; i <= max; i++) {
  ans += i + '\n';
}
console.log(ans);
