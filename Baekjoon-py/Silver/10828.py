import sys

class Stack:
    
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)
    
    def pop(self):
        try:
            return self.items.pop()
        except:
            return -1

    def __len__(self):
        return len(self.items)

    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0
    
    def top(self):
        try:
            return self.items[-1]
        except:
            return -1

N = int(sys.stdin.readline())
s = Stack()
for _ in range(N):
    order = list(map(str, sys.stdin.readline().split()))
    if order[0] == 'push':
        s.push(int(order[1]))
    elif order[0] == 'pop':
        print(s.pop())
    elif order[0] == 'size':
        print(len(s))
    elif order[0] == 'empty':
        print(s.empty())
    else:
        print(s.top())