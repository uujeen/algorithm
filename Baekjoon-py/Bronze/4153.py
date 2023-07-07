import sys
""" 4153번: 직각삼각형 """

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        break
    nums = [a, b, c]
    nums.sort()
    if  (nums[0] ** 2) + (nums[1] ** 2) == nums[2] ** 2:
        print('right')
    else:
        print('wrong')