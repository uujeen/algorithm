import sys
""" 2908번 : 상수 """

li = list(map(str, sys.stdin.readline().split()))

num1 = li[0]
num2 = li[1]
flag = True
for i in range(3):
    if int(num1[2-i]) > int(num2[2-i]):
        break
    elif int(num1[2-i]) < int(num2[2-i]):
        flag = False
        break
    else : continue
    

if flag :
    print(num1[::-1])
else :
    print(num2[::-1])