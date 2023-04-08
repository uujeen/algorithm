import sys, math
""" 백준 2588번 : 곱셈 """
x = str(sys.stdin.readline())
y = str(sys.stdin.readline())

sum = 0
temp = 0
temp_sum = 0
for n in range(3):
    for r in range(3):
        temp = int(int(x[2-r])*math.pow(10,r))*int(y[2-n])
        temp_sum += temp
        
    sum += temp_sum*int(math.pow(10,n))
    print(temp_sum)
    temp_sum = 0
print(int(sum))
