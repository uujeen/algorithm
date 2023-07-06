let input = require('fs')
.readFileSync(__dirname + '/input.txt', {encoding: 'utf-8'})
.split('\n');
let answer = input[0].split('');
let temp = [];
let n = Number(input[1]);
let order, literal;
for(let i = 2; i < n + 2; i++) {
    [order , literal] = input[i].split(' ');
    if(order === 'L') {
        if(answer.length > 0) {
            temp.push(answer.pop());
        }
    }
    else if(order === 'D') {
        if(temp.length > 0) {
            answer.push(temp.pop());
        }
    }
    else if(order === 'B') {
        answer.pop();
    }
    else {
        answer.push(literal);
    }
}
answer = answer.join('') + temp.reverse().join('');
console.log(answer);