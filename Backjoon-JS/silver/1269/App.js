let input = require('fs')
.readFileSync(__dirname + '/input.txt', {encoding: 'utf-8'})
.split('\n');

Set.prototype.intersection = function (set) {
    const result = new Set();

    for (const value of set) {
        // 2개의 set의 요소가 공통되는 요소이면 교집합의 대상이다.
        if (this.has(value)) result.add(value);
    }

    return result;
};

let arrayA = input[1].split(' ');
let arrayB = input[2].split(' ');
let arrayC = arrayA.concat(arrayB);

let set = new Set(arrayC);
let setA = new Set(arrayA);
let setB = new Set(arrayB);
let setC = setA.intersection(setB);
console.log(set);
console.log(setC);
console.log(set.size - setC.size);