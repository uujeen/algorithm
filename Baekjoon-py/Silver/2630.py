import sys

def solution(x, y, N):
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                solution(x, y, N//2)
                solution(x, y + N // 2, N//2)
                solution(x + N // 2, y, N//2)
                solution(x + N // 2, y + N // 2, N//2)
                return
    if color == 0:
        count[0] += 1
    if color == 1:
        count[1] += 1


N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
count = [0, 0]
solution(0, 0, N)
print(count[0])
print(count[1])