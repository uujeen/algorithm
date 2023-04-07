# *을 오른쪽 아래가 직각인 형태로 출력하기

n = int(input('변의 길이를 입력하세요: '))

for i in range(1,n+1):
    print(' '*(n-i), end='')
    print('*'*i)