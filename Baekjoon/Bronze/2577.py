import sys
""" 2577번 : 숫자의 개수 """

A = int(input())
B = int(input())
C = int(input())

li_mul = str(A * B * C)
li= '0123456789'
count =[0]*10
for i in li_mul:
    if li[int(i)] == i:
        count[int(i)] += 1

for i in range(10):
    print(count[i])
    
