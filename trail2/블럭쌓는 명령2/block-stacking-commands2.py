n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
result = [0] * n
for s, e in commands:
    for i in range(s-1,e):
        result[i] += 1
print(max(result))