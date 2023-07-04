let input = require('fs')
.readFileSync(__dirname + '/input.txt', {encoding: 'utf-8'})
.split('\n')[1].split('');
let sum = 0;
let temp = 0;
console.log(input);
input.map((e, idx) => {
    if(Number.isInteger(Number(e))) {
        temp += e;
    }
    else {
        sum += Number(temp);
        temp = 0;
    }
})
sum += Number(temp);
console.log(sum);