import sys

class Stack:
    
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            self.items.pop()
        except:
            return -1
    
    def __len__(self):
        return len(self.items)

T = int(sys.stdin.readline())
for _ in range(T):
    flag = False
    s = Stack()
    vps = list(sys.stdin.readline())
    for i in vps:
        if i == '(':
            s.push(i)
        elif i == ')':
            if s.pop() == -1:
                flag = True
                break
    if len(s) > 0 or flag:
        print('NO')
    else:
        print('YES')