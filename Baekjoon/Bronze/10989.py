import sys
""" 10989번 : 수 정렬하기3 """

def sort(n, x):
    a = [0] * (n + 1)
    for i in x:
        a[i] += 1

    for i in range(1,len(a)):
        while a[i] != 0:
            print(i)
            a[i] -=1
        
    
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    x = [0] * n
    for i in range(n):
        x[i] = int(sys.stdin.readline())
    
    sort(max(x), x)