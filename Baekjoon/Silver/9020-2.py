import sys
""" 9020번 : 골드바흐의 추측 list, dict형태로 구현 후 출력
    딕셔너리 생성에서 실패 생각한 형태의 패턴이 아니였다.
"""

ptr = 0
prime_list = []
prime_list.append(2)
ptr +=1

for i in range(3,10001,2):
    for j in prime_list:
        if i % j == 0:
            break
    else :
        prime_list.append(i)

prime_dict = dict()
prime_dict['4'] = '2 2'
prime_dict['6'] = '3 3'
prime_dict['8'] = '3 5'
prime_dict['10'] = '5 5'
prime_dict['12'] = '5 7'
prime_dict['14'] = '7 7'


for i in range(4,len(prime_list)): # length 1229
    if prime_list[i]>6000: break
    for j in range(i-2,i+1):
        temp = prime_list[j] + prime_list[i]
        prime_dict[str(temp)] = str(prime_list[j]) + ' ' + str(prime_list[i])

print(prime_dict)
# t = int(input())
# for i in range(t):
#     n = int(input()) # 4 <= n >= 10000
#     print(prime_dict[str(n)])