let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
let n = parseInt(input.shift());
let visited = Array.from(Array(n), () => Array.from(n).fill(false));
let graph = Array.from(Array(n), () => input.shift().split(' ').map(Number));
let safetyZone = 0;
let maxSafe = 0;
let dangerZone = 1;
const dy = [-1, 1, 0, 0];
const dx = [0, 0, -1, 1];
const dfs = (y, x) => {
  for (let i = 0; i < 4; i++) {
    ny = dy[i] + y;
    nx = dx[i] + x;
    if (ny >= 0 && ny < n && nx >= 0 && nx < n) {
      if (!visited[ny][nx] && graph[ny][nx] > dangerZone) {
        visited[ny][nx] = true;
        dfs(ny, nx);
      }
    }
  }
};
while (true) {
  if (dangerZone === 100) break;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (!visited[i][j] && graph[i][j] > dangerZone) {
        visited[i][j] = true;
        safetyZone++;
        dfs(i, j);
      }
    }
  }
  if (maxSafe < safetyZone) {
    maxSafe = safetyZone;
  }
  visited = Array.from(Array(n), () => Array.from(n).fill(false));
  safetyZone = 0;
  dangerZone++;
}
console.log(maxSafe);
