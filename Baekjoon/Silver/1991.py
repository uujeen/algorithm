""" 1991번 : 트리 순회"""
n=int(input())

tree=dict()
for _ in range(n):
    root,left,right= map(str, input().split())
    tree[root]=(left,right)

def preorder(root):
    print(root, end='')
    if tree[root][0] != '.':
        preorder(tree[root][0])
    if tree[root][1] != '.':
        preorder(tree[root][1])

def inorder(root):
    if tree[root][0] != '.':
        inorder(tree[root][0])
    print(root, end='')
    if tree[root][1] != '.':
        inorder(tree[root][1])

def postorder(root):
    if tree[root][0] != '.':
        postorder(tree[root][0])
    if tree[root][1] != '.':
        postorder(tree[root][1])
    print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()