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

N = int(sys.stdin.readline())
s = Stack()
for _ in range(N):
    string = int(sys.stdin.readline())
    s.push(string)

tmp = s.pop()
count = 1
for _ in range(len(s)):
    i = s.pop()
    if i > tmp:
        count += 1
        tmp = i

print(count)