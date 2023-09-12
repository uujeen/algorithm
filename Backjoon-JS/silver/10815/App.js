/**
 * myCard
 * checkCard Dict 형태로 저장
 * for문 myCard N
 * for문 Dict 출력 N
 *
 */
// let input = require('fs')
//   .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
//   .split('\n');
// const n = parseInt(input[0]);
// const myCard = [...input[1].split(' ')];
// const m = parseInt(input[2]);
// const checkCard = [...input[3].split(' ')];
// const dict = {};
// for (let i = 0; i < checkCard.length; i++) {
//   let key = checkCard[i];
//   dict[key] = -1;
// }
// for (let i = 0; i < myCard.length; i++) {
//   if (dict[myCard[i]]) {
//     dict[myCard[i]] = 1;
//   }
// }
// const answer = [];
// for (let i = 0; i < checkCard.length; i++) {
//   if (dict[checkCard[i]] === -1) {
//     answer.push(0);
//   } else {
//     answer.push(1);
//   }
// }
// console.log(answer.join(' '));

/**
 * Set 사용
 */
let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
const myCard = new Set(input[1].split(' '));
const checkCard = [...input[3].split(' ')];
let answer = '';
for (let i = 0; i < checkCard.length; i++) {
  if (myCard.has(checkCard[i])) {
    answer += '1 ';
  } else {
    answer += '0 ';
  }
}
console.log(answer);
