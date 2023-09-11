/**
 * 집이 있는 곳 : 1
 * 집이 없는 곳 : 0
 *
 * DFS 재귀적 호출
 * 집이 있는 곳들을 방문하여 단지 갯수 ++;
 * 4방향으로 탐색, 방문하지 않았고, 집이 존재할 때에만 dfs 재귀 호출
 */
let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
const N = parseInt(input[0]);
const arr = [];
for (let i = 1; i < N + 1; i++) {
  arr.push(input[i].split('').map(Number));
}
const visited = Array.from(Array(N), () => Array(N).fill(false));

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

let count = 0;
const dfs = (y, x) => {
  count++;
  for (let i = 0; i < 4; i++) {
    let ny = dy[i] + y;
    let nx = dx[i] + x;
    if (ny >= 0 && ny < N && nx >= 0 && nx < N) {
      if (!visited[ny][nx] && arr[ny][nx]) {
        visited[ny][nx] = true;
        dfs(ny, nx);
      }
    }
  }
};

const house = [];
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (!visited[i][j] && arr[i][j]) {
      visited[i][j] = true;
      count = 0;
      dfs(i, j);
      house.push(count);
    }
  }
}
house.sort((a, b) => {
  return a - b;
});

console.log(house.length);
house.forEach((e) => {
  console.log(e);
});
