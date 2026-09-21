n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = []

for i in grid:
    arr.append(i)

for i in range(n):
    col = []
    for j in range(n):
        col.append(grid[j][i])
    arr.append(col)

ans = 0
for num in arr:
    cnt = 1

    if m == 1:
        ans += 1
        continue

    for i in range(1, n):
        if num[i] == num[i-1]:
            cnt += 1
        else:
            cnt = 1

        if cnt >= m:
            ans += 1
            break        

print(ans)