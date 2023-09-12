let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
const computer = parseInt(input.shift());
const n = parseInt(input.shift());
const graph = [...Array(computer + 1)].map(() => []);
const visited = new Array(computer + 1).fill(false);
let count = 0;
for (let i = 0; i < n; i++) {
  let [a, b] = input[i].split(' ').map(Number);
  graph[a].push(b);
  graph[b].push(a);
}

const dfs = (start) => {
  for (let next of graph[start]) {
    if (!visited[next]) {
      visited[next] = true;
      count++;
      dfs(next);
    }
  }
};

visited[1] = true;
dfs(1);
console.log(count);
