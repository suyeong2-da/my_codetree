n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
k = k-1
for i in range(n):
    flag = True

    for j in range(k, k+m):
        if grid[i][j] == 1:
            flag = False
            break
        
    if not flag:
        if i == 0:
            pass
        else:
            for j in range(k, k+m):
                grid[i-1][j]=1
            break
else:
    for j in range(k, k+m):
        grid[n-1][j]=1

for arr in grid:
    print(*arr)