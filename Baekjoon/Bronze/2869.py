import sys, math
""" 2869번 : 달팽이는 올라가고 싶다. """

A, B, V = map(int, sys.stdin.readline().split())

day = (V-B)/(A-B)

print(math.ceil(day))