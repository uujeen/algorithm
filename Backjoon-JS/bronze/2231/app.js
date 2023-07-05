let input = require('fs')
.readFileSync(__dirname + '/input.txt', {encoding: 'utf-8'})
.split('\n');
let target = Number(input[0]);
let temp = 0;
let str;
for(let i = 0; i <= 1000000; i++) {
    if(i > target) {
        return console.log(0);
    }
    temp = i;
    str = i.toString().split('');
    for(let j = 0; j < str.length; j++) {
        temp += parseInt(str[j]);
    }
    if(target === temp) {
        return console.log(i);
    }
    temp = 0;
}