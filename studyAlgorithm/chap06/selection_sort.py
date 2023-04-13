from typing import MutableSequence
import random

def selection_sort(a: MutableSequence) -> None:
    n = len(a)

    for i in range(n):
        min = i
        for j in range(i+1,n-1):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

    
if __name__ == '__main__':
    n = int(input())
    x = [None] * n
    for i in range(n):
        x[i] = random.randint(1, 100)

    selection_sort(x)
    print(x)