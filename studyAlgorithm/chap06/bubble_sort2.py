from typing import MutableSequence
import random

def bubble_sort(a: MutableSequence) -> None:
    
    n = len(a)
    
    for i in range(n-1):
        for j in range(n-1,i,-1):
            exchange = 0
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchange +=1
        if exchange == 0: # 배열을 한 바퀴 돌아서 교환이 일어나지 않을 경우 반복문 탈출
            break    
    
if __name__ == '__main__':

    n = int(input())
    x = [None] * n
    for i in range(n):
        x[i] = random.randint(0, 100)

    bubble_sort(x)
    print(x)