let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
let n = input.shift();
let k = 2;
let answer = []; // k값들을 저장할 배열
while (true) {
  if (n === '-1') {
    // 종료 조건
    break;
  }
  let coconut = parseInt(n);
  while (k < coconut) {
    // k가 최대값이 되기 위해 coconut보다 작을 때 까지 탐색
    for (let i = 0; i < k; i++) {
      coconut -= 1; // 원숭이에게 한 개
      coconut -= coconut / k; // 내 몫을 제외하고 나머지
      if ((coconut - 1) % k !== 0) {
        // 나누어지는지 확인
        if (i === k - 1) {
          answer.push(k);
        }
        break;
      }
    }
    k++; // 재탐색을 위한 초기화
    coconut = parseInt(n);
  }
  if (answer.length !== 0) {
    // k값이 있을때 없을 때 구분
    console.log(
      n,
      'coconuts,',
      answer[answer.length - 1],
      'people and 1 monkey'
    );
  } else {
    console.log(n, 'coconuts, no solution');
  }
  answer = []; // 초기화
  k = 2;
  n = input.shift();
}
