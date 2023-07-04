let input = require('fs')
.readFileSync(__dirname + '/input.txt', {encoding: 'utf-8'})
.split('\n');
input = Number(input);
let devide = 2;
let arr = [];
while(true) {
    if(input === 1) {
        break;
    }
    if(input % devide == 0) {
        arr.push(devide);
        input = input / devide;
    }
    else {
        devide++;
    }
}
arr.forEach((e) => console.log(e));