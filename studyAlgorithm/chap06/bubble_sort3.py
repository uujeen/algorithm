from typing import MutableSequence
import random

def bubble_sort(a: MutableSequence) -> None:
    
    n = len(a)
    k = 0
    
    while k < n -1:
        last = n-1
        for j in range(n-1, k, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        k = last
    
if __name__ == '__main__':

    n = int(input())
    x = [None] * n
    for i in range(n):
        x[i] = random.randint(0, 100)

    bubble_sort(x)
    print(x)