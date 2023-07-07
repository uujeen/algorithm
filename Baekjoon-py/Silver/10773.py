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
            print("stack이 비어있습니다.")

    def size(self):
        return len(self.items)

K = int(sys.stdin.readline())
s = Stack()
tmp = 0
for _ in range(K):
    order = int(sys.stdin.readline())
    if order == 0:
        s.pop()
    else:
        s.push(order)
for _ in range(s.size()):
    tmp += s.pop()
print(tmp)