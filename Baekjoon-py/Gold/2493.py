import sys
""" 2439번 : 탑 (스택)"""
N = int(sys.stdin.readline())
tops = list(map(int,sys.stdin.readline().split()))
answer= [0] * N
stack = []
#가장 먼저 만나는 높이가 큰 탑에서 수신가능
for i in range(len(tops)):
    while stack:
        if stack[-1][1] < tops[i]: # 스택에 들어있는 탑보다 탐색하는 탑이 더 클 경우 스택에 들어있는 탑은 필요 없기 때문에 삭제
            stack.pop()
        else: # 스택에 들어있는 탑이 더 크기 떄문에 탐색된 탑은 스택에 들어있는 탑에 송신한다
            answer[i] = stack[-1][0] + 1
            break
    stack.append((i, tops[i])) # index, 탑의 높이
print(*answer)