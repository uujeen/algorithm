let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
const max = parseInt(input[0]);
const arr = [];

const Star = (i, j, max) => {
  if (i % 3 === 1 && j % 3 === 1) {
    arr.push(' ');
  } else {
    if (max === 1) {
      arr.push('*');
    } else {
      Star(parseInt(i / 3), parseInt(j / 3), parseInt(max / 3));
    }
  }
};

for (let i = 0; i < max; i++) {
  for (let j = 0; j < max; j++) {
    Star(i, j, max);
  }
  arr.push('\n');
}
console.log(arr.join(''));
