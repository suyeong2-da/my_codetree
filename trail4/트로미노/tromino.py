n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
my_sum = 0
# ---모양
for i in range(n):
    for j in range(m-2):
        s1 = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        if my_sum < s1:
            my_sum = s1

# ---세로 모양
for j in range(m):
    for i in range(n-2):
        s2 = grid[i][j] + grid[i+1][j] + grid[i+2][j]
        if my_sum < s2:
            my_sum = s2

# ㄱ 모양 회전 하는 거
for i in range(n-1):
    for j in range(m-1):
        s3 = grid[i][j] + grid[i+1][j] + grid[i][j+1] + grid[i+1][j+1]
        s3 -= min(grid[i][j], grid[i+1][j], grid[i][j+1], grid[i+1][j+1])
        if my_sum < s3:
            my_sum = s3

print(my_sum)
