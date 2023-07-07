let input = require('fs')
    .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
    .split('\n');
let textArray = input[0].split('');
let bombText = input[1].split('');
let count = 0;
while (true) {
    for (let i = 0; i < textArray.length; i++) {
        for (let j = 0; j < bombText.length; j++) {
            if (textArray[i + j] === bombText[j]) {
                count++;
            } else {
                break;
            }
            if (count === bombText.length) {
                textArray.splice(i, bombText.length);
            }
        }
        count = 0;
        if (textArray.length === 0) {
            return console.log('FRULA');
        }
        if (i === textArray.length) {
            return console.log(textArray.join(''));
        }
    }
}
