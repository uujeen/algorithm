let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
const counts = [
  3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1,
];
let man = input.shift();
let women = input.shift();
let arrayName = [];

const sum = (arr) => {
  if (arr.length === 2) {
    return arr;
  }
  let returnArr = [];
  for (let i = 0; i < arr.length - 1; i++) {
    returnArr.push((arr[i] + arr[i + 1]) % 10);
  }
  return sum(returnArr);
};
for (let i = 0; i < man.length; i++) {
  arrayName.push(counts[man.charCodeAt(i) - 'A'.charCodeAt(0)]);
  arrayName.push(counts[women.charCodeAt(i) - 'A'.charCodeAt(0)]);
}
console.log(sum(arrayName).join(''));
