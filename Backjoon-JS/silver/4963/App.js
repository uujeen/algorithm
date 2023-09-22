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
    for (let i = 0; i < 4; i++) {
      for (let j = 0; j < 4; j++) {
        ny = dy[i] + cy;
        nx = dx[j] + cx;
        if (ny >= 0 && ny < h && nx >= 0 && nx < w) {
          if (!visited[ny][nx] && land[ny][nx] === 1) {
            visited[ny][nx] = true;
            queue.push([ny, nx]);
          }
        }
      }
    }
  }
  answer++;
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
  land = [];
}
