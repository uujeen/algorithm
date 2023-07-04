let input = require('fs')
.readFileSync(__dirname + '/input.txt', {encoding: 'utf-8'})
.split('\n')[0].split('');
let sum = 0;
if(input[0] + input[1] == '0x') {
    input.map((e, idx) => {
        if(idx >= 2) {
            sum += e;
        }
    })
    console.log(parseInt(sum, 16));
}
else if(input[0] == '0') {
    if(input.length == 1) {
        console.log(input); 
    }
    else {        
        input.map((e, idx) => {
            if(idx >= 1) {
                sum += e;
            }
        })
        console.log(parseInt(sum, 8));
    }
}
else {
    console.log(input);
}