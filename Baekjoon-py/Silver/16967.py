import sys
input = sys.stdin.readline
""" 16967번 : 배열 복원하기 """

h, w, x, y = map(int, input().split())
a = [[0] * w for _ in range(h)]
b = []
for _ in range(h + x):
    b.append(list(map(int, input().split())))
for row in range(h + x):
    for col in range(w + y):
        if row < x:
            if col < w:
                a[row][col] = b[row][col] # a의 첫번째 행 값
        elif  x <= row and row < h: # 0번째 인덱스부터 값이 시작하기 떄문에 - 1
            if col < y:
                a[row][col] = b[row][col] # 두번째 행부터 a가 b와 안겹치는 값
            elif y <= col and col < w:
                a[row][col] = b[row][col] - a[row - x][col - y] # 겹치는 값
            else:
                a[row- x][col - y] = b[row][col]
        else:
            if y <= col:
                a[row - x][col - y] = b[row][col] # 안겹치는 값

for i in range(h):
    print(*a[i])