/**
 * n 행, m 열
 * 1. 주어진 팀 컬러를 2차원 배열(graph)로 저장
 * 2. 방문여부를 확인하는 2차원 배열(visited)을 생성
 * 3. 결과를 저장 변수 생성
 * 4. 상하좌우 방향을 위한 direction y, x 배열 생성
 * 5.func dfs 정의
 * 5-1. 방문여부 true 체크
 * 5-2. 4방향에 따라 for문 생성 및 현재 위치 정의
 * 5-3. 현재 위치가 올바른지 확인 만약 아닐 경우 continue.
 * 5-4. 방문 여부 및 팀 색상 체크해서 return시킬 count에 재귀호출
 * 6. 2중 for문으로 graph 탐색
 */
let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');

const [m, n] = input[0].split(' ').map(Number);
const graph = new Array();
for (let i = 1; i < input.length; i++) {
  const a = input[i].split('');
  graph.push(a);
}
// 출력할 팀 값
let white = 0,
  black = 0;
// 상하좌우 방향
const dy = [-1, 1, 0, 0],
  dx = [0, 0, -1, 1];
// 방문여부 확인
const visited = Array.from(Array(n), () => Array(m).fill(false));

/**
 * @param {Number} y y 좌표의 값
 * @param {Number} x x 좌표의 값
 * @param {String} team 팀 생상
 * @param {Number} count 팀 별 카운트를 담는 임의의 변수
 * @returns
 */
function dfs(y, x, team, count) {
  visited[y][x] = true;
  for (let i = 0; i < 4; i++) {
    const ny = y + dy[i],
      nx = x + dx[i];
    if (ny < 0 || nx < 0 || ny >= n || nx >= m) continue;
    if (!visited[ny][nx] && graph[ny][nx] === team)
      count = dfs(ny, nx, team, count + 1);
  }
  return count;
}

/**
 * 1. 방문 여부를 체크
 * 2. 주어진 배열에서 팀 색상을 확인
 */
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (visited[i][j] === true) continue;
    graph[i][j] === 'W'
      ? (white += dfs(i, j, 'W', 1) ** 2)
      : (black += dfs(i, j, 'B', 1) ** 2);
  }
}

console.log(white, black);
