import sys
""" 1065번 : 한수 """

def is_check(x):
    a = x // 100
    b = (x // 10) - (10 * a)
    c = x - (100 * a) - (10 * b)
    # print(f'{x} : {a}, {b}, {c}')
    temp1 = 0
    temp2 = 0
    
    temp1 = a-b
    temp2 = b-c
    temp3 = c-b
    temp4 = b-a

    # print(f'temp : {temp1}, {temp2}')
    if (temp1 == temp2) or (temp3 == temp4):
        return True


n = int(sys.stdin.readline())
count = 0
for i in range(1,n+1):
    if i < 100:
        count += 1
    else:
        if is_check(i):
            count += 1

print(count)