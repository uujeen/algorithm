let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
let [n, m] = input[0].split(' ').map(Number);
let paintsList = [];
for (let i = 1; i < n + 1; i++) {
  paintsList.push(input[i].split(' ').map(Number));
}

let visited = Array.from(Array(n), () => Array(m).fill(false));

let paintsCount = 0;
const dy = [-1, 1, 0, 0];
const dx = [0, 0, -1, 1];

const bfs = (y, x) => {
  let paintWidth = 1;
  const queue = [[y, x]];
  while (queue.length) {
    let [cy, cx] = queue.shift();

    for (let i = 0; i < 4; i++) {
      let ny = dy[i] + cy;
      let nx = dx[i] + cx;

      if (ny >= 0 && ny < n && nx >= 0 && nx < m) {
        if (!visited[ny][nx] && paintsList[ny][nx]) {
          visited[ny][nx] = true;
          paintWidth++;
          queue.push([ny, nx]);
        }
      }
    }
  }
  return paintWidth;
};

let maxWidth = 0;
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (paintsList[i][j] && !visited[i][j]) {
      visited[i][j] = true;
      paintsCount++;
      maxWidth = Math.max(maxWidth, bfs(i, j));
    }
  }
}
console.log(paintsCount);
console.log(maxWidth);
