import sys
""" 2751번 : 수 정렬하기2 """

def merge(a, left, center, right):

    i = left
    k = 0
    j = center + 1
    temp = []
    
    while i <= center and j <= right:
        if a[i] < a[j]:
            temp.append(a[i])
            i += 1

        else:
            temp.append(a[j])
            j += 1
    
    while i <= center:
        temp.append(a[i])
        i += 1
    
    while j <= right:
        temp.append(a[j])
        j += 1
    
    for k in range(left, right + 1):
        a[k] = temp[k-left]

    return a

def merge_sort(a, left, right):
    center = (left + right) // 2
    if left < right:    
        merge_sort(a, left, center)
        merge_sort(a, center+1, right)
        merge(a, left, center, right)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    x = [None] * n
    for i in range(n):
        x[i] = int(sys.stdin.readline())

    merge_sort(x,0,len(x)-1)
    for i in x:
        print(i)