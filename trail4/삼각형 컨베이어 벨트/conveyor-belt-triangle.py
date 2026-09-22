n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
arr = l + r + d

for time in range(t):
    new = []
    new.append(arr.pop())
    new.extend(arr)
    arr = new

print(*arr[:n])
print(*arr[n:2*n])
print(*arr[2*n:])