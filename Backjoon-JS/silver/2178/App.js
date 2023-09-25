let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
const [n, m] = input.shift().split(' ').map(Number);
const graph = input.map((e) => e.split('').map(Number));
const visited = Array.from(Array(n), () => Array(m).fill(false));
const dy = [-1, 1, 0, 0];
const dx = [0, 0, -1, 1];

const bfs = (y, x) => {
  let queue = [[y, x]];
  while (queue.length) {
    const [cy, cx] = queue.shift();
    for (let i = 0; i < 4; i++) {
      const ny = dy[i] + cy;
      const nx = dx[i] + cx;
      if (ny >= 0 && ny < n && nx >= 0 && nx < m) {
        if (!visited[ny][nx] && graph[ny][nx]) {
          visited[ny][nx] = true;
          // 핵심 : bfs로 탐색하면서 다음 위치의 값은 현재 위치에서 1을 더한 값이 되기 때문에
          // 다음 위치는 현재 위치의 값을 더한 값이 되게 하였다.
          graph[ny][nx] += graph[cy][cx];
          queue.push([ny, nx]);
        }
      }
    }
  }
};

bfs(0, 0);
// 최종 위치에 도달헀을때가 결국 0, 0 에서 시작해서 도착지점까지 1씩 더한 값이 되기때문에 최솟값이 된다.
console.log(graph[n - 1][m - 1]);
