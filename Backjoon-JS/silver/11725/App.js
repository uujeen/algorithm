let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
let n = parseInt(input.shift());
let edgeList = input.map((e) => e.split(' ').map(Number));
let rootParent = Array.from(Array(n + 1).keys());
let parent = Array.from(Array(n + 1), () => []);

const find = (v) => {
  if (rootParent[v] !== v) {
    rootParent[v] = find(rootParent[v]);
    return find(rootParent[v]);
  }

  return v;
};

const union = (u, v) => {
  u = find(u);
  v = find(v);
  if (u < v) {
    rootParent[v] = u;
  } else {
    rootParent[u] = v;
  }
};

for (const [u, v] of edgeList) {
  if (find(u) !== find(v)) {
    union(u, v);
  }
}

console.log(parent.join('\n'));
