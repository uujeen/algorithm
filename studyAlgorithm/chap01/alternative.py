# alternative1
# print('n까지 +와-를 번갈아가면서 출력합니다.')
# n = int(input('n을 입력하세요. : '))

# for i in range(n):
#     if i%2:
#         print('-', end='')
#     else:
#         print('+', end='')

# print()

# alternative2
print('n까지 +와-를 번갈아가면서 출력합니다.')

n = int(input('n을 입력하세요. : '))
# // 몫 연산자
for _ in range(n//2):
    print('+-', end='')

if n%2:
    print('+', end='')

print()