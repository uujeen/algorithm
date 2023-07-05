let fs = require('fs')
let input = fs.readFileSync(__dirname + '/input.txt', {encoding : 'utf-8'}).split('\n');
let cardNum = input[0].split(' ')[0];
let target = input[0].split(' ')[1];

let cardArray = input[1].split(' ').sort((a, b) => a - b).map(Number);
let temp;
let min = 0;
for(let i = 0; i < cardNum; i++) {
    for(let j = i + 1; j < cardNum; j++) {
        for(let k = j + 1; k < cardNum; k++) {
            temp = cardArray[i] + cardArray[j] + cardArray[k];
            if(temp <= target && min <= temp) {
                min = temp;
            }
        }
    }
}
console.log(min);