import sys
""" 2562번 : 최댓값 """

list_num = []
for i in range(9):
    a= int(sys.stdin.readline())
    list_num.append(a)

max = list_num[0]
idx = 0 
for i in range(9):
    if list_num[i] > max :
        max = list_num[i]
        idx = i

print(max)
print(idx+1)