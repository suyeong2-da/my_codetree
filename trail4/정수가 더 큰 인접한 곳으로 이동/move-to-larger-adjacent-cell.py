n, r, c = map(int, input().split())
# a = [[0] * (n + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     row = list(map(int, input().split()))
#     for j in range(1, n + 1):
#         a[i][j] = row[j - 1]

grid = [list(map(int, input().split())) for _ in range(n)]
r, c = r-1, c-1
# Please write your code here.
# 우선순위: 상     하     좌      우
direc = [(-1,0), (1,0), (0,-1), (0,1)]
d = 0

result = []
while True:
    nr, nc = r+direc[d][0], c+direc[d][1]
    if 0<=nr<n and 0<=nc<n and grid[nr][nc] > grid[r][c]:
        result.append(grid[r][c])
        r, c = nr, nc
        d = 0
    else:
        d += 1
        if d == 4:
            result.append(grid[r][c])
            break

print(*result)