let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
let [n, ...arr] = input;
arr = arr.map((i) => i.split(' ').map((i) => Number(i)));
for (let i = n - 2; i >= 0; i--) {
  for (let j = 0; j < arr[i].length; j++) {
    arr[i][j] = arr[i][j] + Math.max(arr[i + 1][j], arr[i + 1][j + 1]);
  }
}
console.log(arr[0][0]);
