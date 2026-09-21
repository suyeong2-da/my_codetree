n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n-1):
    minimum = i
    for j in range(i+1, n):
        if arr[j] < arr[minimum]:
            minimum = j
    tmp = arr[i]
    arr[i] = arr[minimum]
    arr[minimum] = tmp
            
print(*arr)