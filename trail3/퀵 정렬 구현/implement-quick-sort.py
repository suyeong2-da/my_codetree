n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def quick(start, end):
    if start >= end:
        return
    
    pivot = start
    l = start+1
    r = end

    while 1:
        while l<=end and arr[l]<=arr[pivot]: l+=1
        while r>start and arr[r]>=arr[pivot]: r-=1

        if l>r: break

        arr[l], arr[r] = arr[r], arr[l]

    arr[pivot], arr[r] = arr[r], arr[pivot]

    quick(start, r-1)
    quick(r+1, end)

quick(0, len(arr)-1)
print(*arr)