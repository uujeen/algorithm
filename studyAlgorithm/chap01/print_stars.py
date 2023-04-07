# print_stars21

# print('*을 출력합니다.')

# n = int(input('몇 개를 출력할까요? :'))
# w = int(input('몇 개마다 줄바꿈할까요? :'))

# for i in range(n):
#     print('*', end='')
#     if i % w == w-1 :
#         print()

# if n % w :
#     print()

# print_stars2

print('*을 출력합니다.')

n = int(input('몇 개를 출력할까요? :'))
w = int(input('몇 번마다 줄바꿈할까요? :'))

for _ in range(n//w):
    print('*'*w)

rest = n %w
if rest:
    print('*'*rest)