n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def merge(start, end):
    if start==end:
        return
    mid = (start+end)//2

    merge(start, mid)
    merge(mid+1, end)

    a = start
    b = mid+1
    result = []

    while 1:
        if a>mid and b>end: break
        if a>mid:
            result.append(arr[b])
            b+=1
        elif b>end:
            result.append(arr[a])
            a+=1
        elif arr[a]<=arr[b]:
            result.append(arr[a])
            a+=1
        else:
            result.append(arr[b])
            b+=1
    for i in range(len(result)):
        arr[start+i] = result[i]

merge(0, len(arr)-1)
print(*arr)