n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
boom = grid[r-1][c-1]
grid[r-1][c-1] = 0

d = [(-1,0), (1,0), (0,-1), (0,1)]
for dr, dc in d:
    for k in range(1, boom):
        nr, nc = (r-1)+dr*k , (c-1)+dc*k
        if 0<=nr<n and 0<=nc<n:
            grid[nr][nc] = 0

new_grid = []

for j in range(n):
    arr = []
    num = []
    for i in range(n):
        if grid[i][j] == 0:
            arr.append(grid[i][j])
        else:
            num.append(grid[i][j])
    new_grid.append(arr+num)

for j in range(n):
    for i in range(n):
        print(new_grid[i][j], end=' ')
    print()