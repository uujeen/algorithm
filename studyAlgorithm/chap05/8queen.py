# 8퀸 문제 알고리즘 구현

pos = [0] * 8
flag_a = [False] * 8 # 각 행에 1개씩 배치
flag_b = [False] * 15 # 우측 대각선 방향 체크
flag_c = [False] * 15 # 좌측 대각선 방향 체크

def put():
    for i in range(8):        
        print(f'{pos[i]:2}', end='')
    print()

def set(i):
    for j in range(8):
        if (not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + 7]):
            pos[i] = j
            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i+1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False
                

set(0)
print(count)