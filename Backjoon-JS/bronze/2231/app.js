let input = require('fs')
.readFileSync(__dirname + '/input.txt', {encoding: 'utf-8'})
.split('\n');
let target = Number(input[0]);
let temp = 0;
let i, str;
for(i = 0; i <= 1000000; i++) {
    if(i > target) {
        temp = 0;
        break;
    }
    temp = i;
    str = i.toString();
    str.split('')
    for(let j = 0; j<str.length; j++) {
        temp += parseInt(str[j]);
    }
    if(target === temp) {
        break;
    }
    temp = 0;
}
if(temp !== 0) {
    console.log(i);
}
else {
    console.log(0);
}