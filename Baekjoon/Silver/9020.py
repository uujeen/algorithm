import sys
""" 9020번 : 골드바흐의 추측 """

def is_prime_number(v):
    for i in range(2, v):
        if v % i == 0:
            return False
    return True
        
t = int(input())
val2 = 0
for i in range(t):
    n = int(input()) # 4 <= n >= 10000
    value = n // 2
    if is_prime_number(value):
        print(f'{value} {value}')
    else:
        for i in range(value,2,-1):
            if is_prime_number(i) :
                temp = value - i
                val2 = value + temp
                if is_prime_number(val2):
                    print(f'{i} {val2}')
                    break