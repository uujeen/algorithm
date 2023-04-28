import sys
memozation = [0] * 100

def fibo(n):
    if n == 1 or n == 2:
        return 1
    if memozation[n] != 0:
        return memozation[n]
    memozation[n] = fibo(n - 1) + fibo(n - 2)
    return memozation[n]
    
n = int(sys.stdin.readline().rstrip())
print(fibo(n))