import random
from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)

    for i in range(n-1):
        for j in range(n-1,i,-1):
            if a[j-1]>a[j]:
                a[j-1], a[j] = a[j], a[j-1]

if __name__ == '__main__':
    num = int(input())
    x = [None] * num

    for i in range(num):
        x[i] = random.randint(1, 100)
    
    bubble_sort(x)

    print(x)