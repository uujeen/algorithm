let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
let n = parseInt(input.shift());
let q = parseInt(input.shift());
let arr = Array(n + 1).fill(0);
let dp = Array(1000000).fill(0);
for (let i = 0; i <= n; i++) {
  if (i <= 1) {
    dp[i] = i;
  } else {
    dp[i] = dp[i - 2] + dp[i - 1];
  }
}
for (let i = 0; i < q; i++) {
  const [start, end] = input.shift().split(' ').map(Number);
  for (let i = start; i <= end; i++) {
    arr[i] += dp[i - start + 1];
  }
}

arr = arr.map((e) => {
  return e % (Math.pow(10, 9) + 7);
});
console.log(arr.slice(1).join(' '));
