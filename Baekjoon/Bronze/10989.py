import sys
""" 10989번 : 수 정렬하기3 """

def fsort(a, max_a):
    n = len(a)
    f = [0] * (max_a+1)
    b = [0] * n

    for i in range(n): f[a[i]] += 1
    for i in range(1, max_a + 1): f[i] += f[i - 1]
    for i in range(n - 1, -1, -1): f[a[i]] -= 1; b[f[a[i]]] = a[i]
    for i in range(n): a[i] = b[i]

def counting_sort(a):
    fsort(a, max(a))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    x = [None] * n
    for i in range(n):
        x[i] = int(sys.stdin.readline())

    counting_sort(x)
    for i in range(len(x)):
        print(x[i])