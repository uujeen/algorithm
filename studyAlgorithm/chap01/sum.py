print('a부터 b까지의 합을 구합니다.')
a = int(input('a값을 입력하세요. :'))
b = int(input('b값을 입력하세요. :'))


if a>b : a,b = b,a 
sum = 0
for i in range(a,b+1,1):
    sum +=i

print(f'{a}부터 {b}까지의 합 : {sum}')