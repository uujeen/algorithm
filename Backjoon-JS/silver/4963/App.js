let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
let w = 1;
let h = 1;
let visited = [];
let land = [];
let answer = 0;
const dy = [-1, 1, 0, 0];
const dx = [0, 0, -1, 1];

const bfs = (y, x) => {
  const queue = [];
  queue.push([y, x]);
  while (queue.length !== 0) {
    const [cy, cx] = queue.shift();
    // 핵심 : 대각선도 연결된 섬이기 때문에 다음 섬으로 가기위한 방향을 정할 때 이중 for문을 사용해 대각선도 체크한다.
    for (let i = 0; i < 4; i++) {
      for (let j = 0; j < 4; j++) {
        ny = dy[i] + cy;
        nx = dx[j] + cx;
        // BFS 탐색 하듯이 queue가 빌 때 까지 반복하며 연결된 섬을 찾는다.
        // 방향이 탐색범위를 넘지 않는지 파악하고 해당 섬을 방문표시를 하며 queue에 삽입한다.
        if (ny >= 0 && ny < h && nx >= 0 && nx < w) {
          if (!visited[ny][nx] && land[ny][nx] === 1) {
            visited[ny][nx] = true;
            queue.push([ny, nx]);
          }
        }
      }
    }
  }
  answer++; // queue를 다 탐색했을 경우 answer에 연결된 섬의 개수를 추가한다.
};

while (true) {
  [w, h] = input.shift().split(' ').map(Number);
  if (w === 0 && h === 0) {
    break;
  }
  visited = Array.from(Array(h), () => Array(w).fill(false));
  answer = 0;
  for (let i = 0; i < h; i++) {
    land[i] = input.shift().split(' ').map(Number);
  }
  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (!visited[i][j] && land[i][j]) {
        visited[i][j] = true;
        bfs(i, j);
      }
    }
  }
  console.log(answer);
}
