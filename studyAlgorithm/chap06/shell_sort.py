from typing import MutableSequence
import random

def shell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 2
    

if __name__ == '__main__':

    num = int(input())
    x = [None] * num
    for i in range(num):
        x[i] = random.randint(1, 100)
    shell_sort(x)
    print(x)
