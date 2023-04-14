from typing import Sequence

def seq_search(a: Sequence, key: Any) -> int:

    n = len(a)
    for i in range(n):
        if key == a[i]:
            return i
    return -1
# 보초법 적용한 seq_search

def seq_search_sentinel(a, key):
    sentinel = a.deepcopy(a)
    sentinel.append(key)
    i = 0
    while True:
        if sentinel[i] == key:
            break
        i +=1
    return -1 if i == len(sentinel) else i # 리턴 되는 값이 원래 배열의 값인지 보초 배열에 있는 값인지 판단하기 위해 만약 i 가 보초값에 있던 것이라면 -1 아닐 경우 i 반환
if __name__ == '__main__':
    n = int(input)
    x = [None] * n
    for i in range(n):
        x[i] = int(input(f'x{[i]} : '))
    key = int(input('찾을 키 값은? : '))
    
    if seq_search(x, key) != -1:
        print(f'{key} 값은 {seq_search(x, key)} 인덱스에 존재한다.')
    else:
        print('찾는 {key}값은 존재하지 않습니다.')