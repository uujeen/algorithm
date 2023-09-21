let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');

const n = parseInt(input.shift());
const [row, col] = input.shift().split(' ').map(Number);
let points = new Map();
let answer = 0;
input.forEach((e) => {
  const [x, y] = e.split(' ').map(Number);
  points.set(`${x}, ${y}`, 1);
});

for (const item of input) {
  const [x, y] = item.split(' ').map(Number);
  if (!points.has(`${x + row}, ${y}`)) continue;
  if (!points.has(`${x}, ${y + col}`)) continue;
  if (!points.has(`${x + row}, ${y + col}`)) continue;
  answer++;
}

console.log(answer);
