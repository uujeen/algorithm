print('세 정수의 최댓값을 구합니다.')

a = int(input('정수 a의 값을 입력하세요. :'))
b = int(input('정수 b의 값을 입력하세요. :'))
c = int(input('정수 c의 값을 입력하세요. :'))

def max(a, b, c):
    maximum = a
    
    if b > maximum : maximum = b
    if c > maximum : maximum = c

    return maximum

print(f'최댓값은 {max(a,b,c)}입니다.')

