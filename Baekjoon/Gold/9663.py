import sys
""" 9663번 : N-Queen """

def set(i):
    for j in range(N):
        global count
        if (not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + (N - 1)]):
            pos[i] = j
            if i == N-1:
                count += 1
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (N - 1)] = True
                set(i+1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (N - 1)] = False
                
if __name__ == '__main__':
    N = int(sys.stdin.readline())

    pos = [0] * N # 각 열에 퀸을 한 개씩 배치하기
    flag_a = [False] * N # 각 행에 퀸을 한 개씩 배치하기
    flag_b = [False] * (2 * N - 1) # 우측 대각선방향 배치 체크
    flag_c = [False] * (2 * N - 1) # 좌측 대각선방향 배치 체크
    count = 0
    set(0)
    print(count)