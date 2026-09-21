n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_sum = 0
for i in range(n-2):
    for j in range(n-2):
        sum = 0
        for k in range(3):
            for l in range(3):
                sum += grid[i+k][j+l]
        if sum >= max_sum:
            max_sum = sum

print(max_sum)