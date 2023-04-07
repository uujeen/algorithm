# 구구단 곱셈표 출력하기

print('-'*27)

for i in range(1,10):
    for j in range(1,10):
        """ i * j의 숫자를 3자리로 출력 """
        print(f'{i*j:3}', end='')
    print()

print('-'*27)
    