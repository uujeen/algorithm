import sys
""" 백준 1085번 : 직사각형에서 탈출 """

x, y, w, h = map(int,sys.stdin.readline().split())

distx = 0
disty = 0
if w-x < x: distx = w-x
else: distx = x

if h-y < y: disty = h-y
else: disty = y

if distx <disty:print(distx)
else: print(disty)