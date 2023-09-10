let input = require('fs')
  .readFileSync(__dirname + '/input.txt', {
    encoding: 'utf-8',
  })
  .split('\n');

let [N, K] = input[0].split(' ').map(Number);
let wordsList = input.slice(1, N + 1); // 받은 문자열 저장
let alphabetArr = new Array(26).fill(0); // 전체 알파벳 배열 저장 0, 1로 배웠는지 안배웠는지 여부 판단
let readCount = K - 5; // a, c, i, n, t는 기본적으로 배워야하기 때문에 K - 5
let answer = 0; // 정답

if (readCount < 0) {
  // 기본 단어를 배울 수 없는 경우기 때문에 0 반환
  console.log(0);
  return;
}

// 각각 a,c,i,n,t
alphabetArr[0] = 1;
alphabetArr[2] = 1;
alphabetArr[8] = 1;
alphabetArr[13] = 1;
alphabetArr[19] = 1;

let dfs = (index, readCount) => {
  if (readCount < 0) {
    // 종료조건
    return;
  }

  if (readCount === 0) {
    // 배울 수 있는 알파벳을 다 배웠을 때
    let count = 0;
    for (let i = 0; i < N; i++) {
      // 입력받은 문자열에 접근하여 해당 알파벳들로 완성된 단어가 있는지 확인
      let flag = true; // 완성된 단어인지 확인하기 위한 flag
      for (let j = 0; j < wordsList[i].length; j++) {
        if (alphabetArr[wordsList[i][j].charCodeAt() - 97] === 0) {
          // 문자열의 알파벳들을 확인하여 배웠는지 체크
          flag = false; // 안배웠던 단어라면 완성되지 않았기 때문에 false로 주고
          break; // for문 탈출
        }
      }
      if (flag) count++;
    }
    answer = Math.max(answer, count); // 매 순간 가장 큰 값을 갖기 위해 확인
  }

  for (let i = index; i < 26; i++) {
    // 알파벳 배열의 전체를 방문
    if (alphabetArr[i] === 0) {
      // 만약 아직 안배웠다면
      alphabetArr[i] = 1; // 배우고
      console.log('확인용' + readCount);
      dfs(i, readCount - 1); // 재탐색, 배웠기 때문에 count 감소
      alphabetArr[i] = 0; // 탐색 완료했기 때문에 0으로 초기화
    }
  }
};

dfs(0, readCount);

console.log(answer);
