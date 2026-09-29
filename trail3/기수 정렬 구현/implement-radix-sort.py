n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def radix_sort(arr, k):
    for pos in range(k-1, -1, -1):
        arr_new = [[] for _ in range(10)]
        for i in range(len(arr)):
            num = str(arr[i]).zfill(k)
            digit = int(num[pos])
            arr_new[digit].append(arr[i])
        store_arr = []
        for i in range(10):
            for j in range(len(arr_new[i])):
                store_arr.append(arr_new[i][j])
        arr = store_arr
    return arr

k = len(str(max(arr)))
result = radix_sort(arr, k)
print(*result)