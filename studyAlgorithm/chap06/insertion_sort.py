from typing import MutableSequence
import random

def insertion_sort(a: MutableSequence) -> None:

    n = len(a)
    for i in range(n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

if __name__ == '__main__':

    num = int(input())
    x = [None] * num
    for i in range(num):
        x[i] = random.randint(1, 100)
    insertion_sort(x)
    print(x)
