from typing import MutableSequence
import random
# 셰이커 정렬 알고리즘 구현하기

def shaker_sort(a: MutableSequence) -> None:
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for i in range(right, left, -1):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
                last = i
        left = last

        for i in range(left, right):
            if a[i + 1] > a[i]:
                a[i + 1], a[i] = a[i], a[i + 1]
                last = i
        right = last

if __name__ == '__main__':
    n = int(input())

    x = [None] * n

    for i in range(n):
        x[i] = random.randint(1,100)
    
    shaker_sort(x)
    print(x)