let input = require('fs')
    .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
    .split('\n');
let name, age, weight;
for (let i = 0; i < input.length; i++) {
    [name, age, weight] = input[i].split(' ');

    if (name + ' ' + age + ' ' + weight === '# 0 0') {
        break;
    }
    if (age > 17 || weight > 80) {
        console.log(name, 'Senior');
    } else {
        console.log(name, 'Junior');
    }
}
