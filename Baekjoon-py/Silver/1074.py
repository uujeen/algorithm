import sys
""" 1074번 : Z 
1. (N) 짝수 행, 열의 값은 (N-1) 행//2, 열//2의 값의 4배이다.
2. 만약 홀수의 행 또는 열, (행, 열)의 경우 (2*(r%2))+c%2의 식을 통해 Z방향으로의 움직임으로 짝수 행, 열의 값에서 + (1, 2, 3)으로 값을 가진다.
3. N 사이즈의 Square -> N-1 사이즈의 Square로 재귀적 호출 진행
"""

def z_search(N, r, c):
    if N == 0:
        return 0

    return 4*z_search(N-1, r//2, c//2) + (2*(r%2))+c%2


N, r, c = map(int, sys.stdin.readline().split())
print(z_search(N, r, c))