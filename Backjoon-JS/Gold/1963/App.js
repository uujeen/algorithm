/**
 * N번만큼 bfs로 탐색하는데 isPrime을 사용하여 true일 경우에만 count 증가 queue에 삽입
 * 중요 포인트 : 문자열에서 특정 인덱스의 문자를 하나씩 바꾸기
 * 해당 숫자에 도달했을 때 현재 방문한 숫자에서 더하기 1
 */
let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
let start, end;
let visited = [];
let changed = [];

// 문자열에서 특정 인덱스의 문자 변환하는 함수
String.prototype.replaceAt = function (index, replacement) {
  return (
    this.slice(0, index) + replacement + this.slice(index + replacement.length)
  );
};

const isPrime = (num) => {
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
};

const bfs = (start, end) => {
  const queue = [start];
  visited[start] = true;
  changed[start] = 0;

  while (queue.length) {
    const current = queue.shift();

    for (let i = 0; i < 4; i++) {
      for (let j = 0; j < 10; j++) {
        const next = current.replaceAt(i, String(j));

        if (next < 1000 || next > 9999 || visited[next] || !isPrime(next)) {
          continue;
        }
        visited[next] = true;
        changed[next] = changed[current] + 1;
        queue.push(next);

        if (next === end) return;
      }
    }
  }
};

for (let i = 1; i < input.length; i++) {
  [start, end] = input[i].split(' ');
  visited = Array(10000).fill(false);
  changed = Array(10000).fill(-1);
  bfs(start, end);
  console.log(changed[end] === -1 ? 'Impossible' : changed[end]);
}
