from typing import Any, Sequence
import random
"""
이미 오름차순으로 정렬된 리스트에 사용 가능
정렬되지 않은 리스트일 경우 선형탐색 (linear_search) 사용
"""
def binary_search(a, key):
    left = 0
    right = len(a) - 1
    center = (left + right) // 2
    while True:
        if a[center] == key:
            return center
        elif a[center] > key:
            right = center - 1
            center = (left + right) // 2
        else:
            left = center +1
            center = (left + right) // 2
        if left > right:
            break
    return -1

def binary_search_recur(a, key, left, right):
    center = (left + right) // 2
    if a[center] == key:
        return center
    elif a[center] > key:
        binary_search_recur(a, key, left, center - 1)
    else:
        binary_search_recur(a, key, center + 1, right)


def merge_sort(a, left, center, right):
    i = left
    k = 0
    j = center + 1
    tmp = []

    while i <= center and j <= right:
        if a[i] < a[j]:
            tmp.append(a[i])
            i += 1

        else:
            tmp.append(a[j])
            j += 1
    
    while i <= center:
        tmp.append(a[i])
        i += 1
    
    while j <= right:
        tmp.append(a[j])
        j += 1
    
    for k in range(left, right + 1):
        a[k] = tmp[k-left]

    return a

def merge(a, left, right):
    center = (left + right) // 2
    if left < right:
        merge(a, left, center)
        merge(a, center + 1, right)
        merge_sort(a, left, center, right)

if __name__ == '__main__':
    n = int(input())
    x = [None] * n
    for i in range(n):
        x[i] = random.randint(1, 100)
    key = random.choice(x) 
    merge(x, 0 , n-1)
    print(f'키 값 {key}은 인덱스 {binary_search(x, key)}에 있습니다.')
            
