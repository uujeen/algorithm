import sys
input = sys.stdin.readline
""" 1541번: 잃어버린 괄호 """

pre_state = str(input().rstrip())
in_state = pre_state.split('-')
arr = []
temp = []

for state in in_state:
    tmp = state.split('+')
    for val in tmp:
        num = int(val)
        temp.append(num)
    arr.append(sum(temp))
    temp = []

answer = arr.pop(0)

for val in arr:
    answer -= val
    
print(answer)