let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
let [n, k] = input.shift().split(' ').map(Number);
let arr = input.shift().split('');
let answer = 0;
for (let i = 0; i <= n; i++) {
  if (arr[i] === 'P') {
    for (let j = i - k; j <= i + k; j++) {
      if (arr[j] === 'H') {
        arr.splice(i, 1, 'C');
        arr.splice(j, 1, 'C');
        answer++;
        break;
      }
    }
  } else if (arr[i] === 'H') {
    for (let j = i - k; j <= i + k; j++) {
      if (arr[j] === 'P') {
        arr.splice(i, 1, 'C');
        arr.splice(j, 1, 'C');
        answer++;
        break;
      }
    }
  }
}

console.log(answer);
