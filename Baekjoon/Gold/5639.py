import sys
""" 5639번: 이진 검색 트리 """
sys.setrecursionlimit(10**6)

pre_tree = []

while True:
    try:
        pre_tree.append(int(sys.stdin.readline()))
    except:
        break

def binary_search_tree(tree):
    sub_left = []
    sub_right = []
    if tree:
        root = tree.pop(0)
        for node in tree:
            if node < root:
                sub_left.append(node)
            else:
                sub_right.append(node)                
        binary_search_tree(sub_left)
        binary_search_tree(sub_right)
        print(root)

binary_search_tree(pre_tree)
