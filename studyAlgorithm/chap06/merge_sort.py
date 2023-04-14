from typing import MutableSequence
import random
def my_merge(a, left, center, right):

    i = left
    k = 0
    j = center + 1
    temp = []
    
    while i <= center and j <= right:
        if a[i] < a[j]:
            temp.append(a[i])
            i += 1

        else:
            temp.append(a[j])
            j += 1
    
    while i <= center:
        temp.append(a[i])
        i += 1
    
    while j <= right:
        temp.append(a[j])
        j += 1
    
    for k in range(left, right + 1):
        a[k] = temp[k-left]

    return a

def my_merge_sort(a, left, right):
    center = (left + right) // 2
    if left < right:    
        my_merge_sort(a, left, center)
        my_merge_sort(a, center+1, right)
        my_merge(a, left, center, right)

"""
def merge_sort(a: MutableSequence) -> None:


    def _merge_sort(a: MutableSequence, left:int, right:int) -> None:

        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)
            _merge_sort(a, center + 1, right)

            p = j = 0
            i = k = left
            
            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1


    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0, n - 1)
    del buff
"""


if __name__ == '__main__':
    print('병합 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num

    for i in range(num):
        x[i] = random.randint(1, 100)

    # merge_sort(x)
    my_merge_sort(x, 0, len(x)-1)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'f[{i}] = {x[i]}')
