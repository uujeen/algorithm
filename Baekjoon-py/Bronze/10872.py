import sys
""" 10872번 : 팩토리얼 """

def fact(x):
    if x>0:
        return x*fact(x-1)
    else:
        return 1

N = int(input())
print(fact(N))