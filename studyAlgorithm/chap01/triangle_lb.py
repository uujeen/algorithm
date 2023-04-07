# *을 왼쪽 아래가 직각인 삼각형 모양으로 출력하기

n = int(input('짧은 변의 길이를 입력하세요: '))

for i in range(1,n+1):
    print('*'*i,end='')
    print(' '*(n-i))