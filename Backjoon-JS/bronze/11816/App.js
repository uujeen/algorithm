let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n')[0];
const array = input.split('');
let flag = false;
if (array[0] === '0') {
  if (array[1] === 'x') {
    console.log(parseInt(input, 16));
    flag = true;
  } else {
    console.log(parseInt(input, 8));
    flag = true;
  }
}
if (!flag) {
  console.log(input);
}
