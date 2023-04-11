import sys
""" 2628번 : 종이자르기 """

x, y =  map(int,sys.stdin.readline().split()) # max = 100cm
t = int(sys.stdin.readline())
area = 0
x_list = [0]
y_list = [0]
x_list.append(x)
y_list.append(y)

for _ in range(t):
    cut = list(map(int,sys.stdin.readline().split()))
    if cut[0] == 0:
        y_list.append(cut[1])
    else:
        x_list.append(cut[1])

x_list = sorted(x_list)
y_list = sorted(y_list)

max_x = []
max_y = []
for i in range(0,len(x_list)-1):
    max_x.append(abs(x_list[i+1]-x_list[i]))
for i in range(0,len(y_list)-1):
    max_y.append(abs(y_list[i+1]-y_list[i]))
area = max(max_x)*max(max_y)
print(area)