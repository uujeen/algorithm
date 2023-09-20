/**
 * 연결 리스트로 구현
 * value와 다음 노드를 가리킬 next
 */
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

/**
 * queue의 head와 tail로 리스트의 구조를 정의
 * size를 통해 queue의 길이를 저장
 */
class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }
  /**
   * value를 받아 새로운 노드 생성
   * queue가 비었을 경우 head와 tail에 해당 노드 저장
   * 아닐 경우, queue의 tail을 갱신하고 size 증가
   * @param {value} value
   */
  enqueue(value) {
    const newNode = new Node(value);

    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }

    this.size++;
  }
  /**
   * queue가 비었을 경우 -1반환
   * 아닐 경우, head의 노드를 삭제하기 위해 저장 및 head를 head.next값으로 변경
   * 만약 리스트가 하나의 노드만 존재했다면 tail에 null값을 갱신, size 감소
   * @returns 삭제할 노드
   */
  dequeue() {
    if (!this.head) {
      return -1;
    }

    const removeNode = this.head;
    this.head = this.head.next;
    if (!this.head) {
      this.tail = null;
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

  ishead() {
    if (this.size === 0) {
      return -1;
    }
    return this.head.value;
  }

  isBack() {
    if (this.size === 0) {
      return -1;
    }
    return this.tail.value;
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
  } else if (order === 'head') {
    answer.push(q.ishead());
  } else {
    answer.push(q.isBack());
  }
}
console.log(answer.join('\n'));
