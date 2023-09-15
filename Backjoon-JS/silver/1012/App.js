let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
let testCase = parseInt(input.shift());

const dy = [-1, 1, 0, 0];
const dx = [0, 0, -1, 1];
let count, visited, graph;
let m, n, k;
const dfs = (y, x) => {
  for (let i = 0; i < 4; i++) {
    ny = dy[i] + y;
    nx = dx[i] + x;
    if (ny >= 0 && ny < n && nx >= 0 && nx < m) {
      if (!visited[ny][nx] && graph[ny][nx]) {
        visited[ny][nx] = true;
        dfs(ny, nx);
      }
    }
  }
};

for (let i = 0; i < testCase; i++) {
  [m, n, k] = input.shift().split(' ').map(Number);
  visited = Array.from(Array(n), () => Array(m).fill(false));
  graph = Array.from(Array(n), () => Array(m).fill(0));
  count = 0;

  for (let j = 0; j < k; j++) {
    const [x, y] = input.shift().split(' ').map(Number);
    graph[y][x] = 1;
  }

  for (let k = 0; k < n; k++) {
    for (let u = 0; u < m; u++) {
      if (!visited[k][u] && graph[k][u]) {
        visited[k][u] = true;
        count++;
        dfs(k, u);
      }
    }
  }
  console.log(count);
}
