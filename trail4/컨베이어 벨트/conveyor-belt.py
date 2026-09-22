n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
arr = u + d

for time in range(t):
    new = []
    new.append(arr.pop())
    new.extend(arr)
    arr = new

print(*arr[:n])
print(*arr[n:])
