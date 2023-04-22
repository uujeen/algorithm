from typing import MutableSequence
import random

def heapify(a: MutableSequence, left, right) -> None:
    largest = left
    cl = 2 * left + 1
    cr = 2 * left + 2
    if cl < right and a[cl] > a[largest]:
        largest = cl
    if cr < right and a[cr] > a[largest]:
        largest = cr
    if largest != left:
        a[largest], a[left] = a[left], a[largest]
        heapify(a, largest, right)
        
def heap_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2, -1, -1): # 최대힙트리로 정렬
        heapify(a, i, n)
    # for i in range(n - 1, -1, -1): # 최소힙트리로 정렬
    #     a[0], a[i] = a[i], a[0]
    #     heapify(a, 0, i)
    return a

if __name__ == '__main__':

    num = int(input())
    x = [None] * num
    for i in range(num):
        x[i] = random.randint(1, 100)
    heap_sort(x)
    print(x)
