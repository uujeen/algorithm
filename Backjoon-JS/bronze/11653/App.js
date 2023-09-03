let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
input = Number(input);
let devide = 2;
let arr = [];
while (true) {
  if (input === 1) {
    return;
  }
  if (input % devide === 0) {
    arr += devide + '\n';
    input = input / devide;
  } else {
    devide++;
  }
}
console.log(arr);
