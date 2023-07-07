import sys
""" 1914번 : 하노이 탑 """

def hanoi_top(n, start, middle, end):
    if n == 1:
        print(start, end)
    else:
        hanoi_top(n-1, start, end, middle)
        hanoi_top(1, start, middle, end)
        hanoi_top(n-1, middle, start, end)

def sum(n):
    if n == 1: return 1
    else:        
        return 2**(n-1)+sum(n-1)

N = int(sys.stdin.readline())

start = 1
middle = 2
end = 3
print(sum(N))
if N <=20:
    hanoi_top(N, start, middle, end)