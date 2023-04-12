import sys
""" 9663번 : N-Queen """

def set(i):
    for j in range(N):
        global count
        if (not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + (N - 1)]): 
            pos[i] = j
            if i == N-1: # 해당 행을 다 채우면 count 1 증가
                count += 1
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (N - 1)] = True # 배치 했기 떄문에 체크
                set(i+1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (N - 1)] = False # 퀸을 j 행에서 제거해야 하므로 False로 전환
                
if __name__ == '__main__':
    N = int(sys.stdin.readline())

    pos = [0] * N # 각 열에 퀸을 한 개씩 배치하기
    flag_a = [False] * N # 각 행에 퀸을 한 개씩 배치하기
    flag_b = [False] * (2 * N - 1) # 우측 대각선방향 배치 체크
    flag_c = [False] * (2 * N - 1) # 좌측 대각선방향 배치 체크
    count = 0
    set(0)
    print(count)