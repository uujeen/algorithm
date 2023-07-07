import sys
input = sys.stdin.readline

while True:
    try:
        a, b = map(int, input().split())
        if a == b == 0:
            break
        print(a + b)
    except:
        break