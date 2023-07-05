let input = require('fs')
.readFileSync(__dirname + '/input.txt', {encoding: 'utf-8'})
.split('\n');
let answer = input[0].split('\n');
let n = Number(input[1]);
let order, literal;
let len = answer.length;
let cursor = len;
for(let i = 2; i < n + 2; i++) {
    [order , literal] = input[i].split(' ');
    if(order === 'L') {
        if(cursor>0) {
            cursor--;
        }
    }
    else if(order === 'D') {
        if(cursor < len) {
            cursor++;
        }
    }
    else if(order === 'B') {
        answer[cursor] = '';
    }
    else {
        answer[cursor] += literal;
    }
}
console.log(answer);