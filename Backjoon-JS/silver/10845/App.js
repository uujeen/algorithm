class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.front = null;
    this.rear = null;
    this.size = 0;
  }

  enqueue(data) {
    const newNode = new Node(data);

    if (!this.front) {
      this.front = newNode;
      this.rear = newNode;
    } else {
      this.rear.next = newNode;
      this.rear = newNode;
    }

    this.size++;
  }

  dequeue() {
    if (!this.front) {
      return -1;
    }

    const removeNode = this.front;
    this.front = this.front.next;
    if (!this.front) {
      this.rear = null;
    }

    this.size--;

    return removeNode.value;
  }

  len() {
    return this.size;
  }

  isEmpty() {
    if (this.size === 0) {
      return 1;
    }
    return 0;
  }

  isFront() {
    if (this.size === 0) {
      return -1;
    }
    return this.front.value;
  }

  isBack() {
    if (this.size === 0) {
      return -1;
    }
    return this.rear.value;
  }
}

let input = require('fs')
  .readFileSync(__dirname + '/input.txt', { encoding: 'utf-8' })
  .split('\n');
let n = parseInt(input.shift());
const q = new Queue();
const answer = [];
for (let i = 0; i < n; i++) {
  const [order, value] = input.shift().split(' ');

  if (order === 'push') {
    q.enqueue(value);
  } else if (order === 'pop') {
    answer.push(q.dequeue());
  } else if (order === 'size') {
    answer.push(q.len());
  } else if (order === 'empty') {
    answer.push(q.isEmpty());
  } else if (order === 'front') {
    answer.push(q.isFront());
  } else {
    answer.push(q.isBack());
  }
}
console.log(answer.join('\n'));
