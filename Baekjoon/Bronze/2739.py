import sys
""" 백준 2739번 : 구구단 """

n = int(sys.stdin.readline())

for i in range(1,10):
    print(f'{n} * {i} = {n*i}')