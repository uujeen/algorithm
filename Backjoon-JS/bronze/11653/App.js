let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
input = parseInt(input);
let devide = 2;
let arr = '';

while (true) {
  if (devide > input) {
    break;
  }
  if (input % devide === 0) {
    input = input / devide;
    arr += devide + '\n';
    devide = 1;
  }
  devide++;
}
console.log(arr);
