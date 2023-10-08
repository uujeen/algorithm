let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
let t = parseInt(input.shift());
while (true) {
  if (t === 0) break;
  t--;
  let numsCount = parseInt(input.shift());
  let nums = input.shift().split(' ').map(Number);
  nums.sort((a, b) => a - b);
  console.log(nums[0], nums[numsCount - 1]);
}
