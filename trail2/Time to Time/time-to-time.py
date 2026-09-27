a, b, c, d = map(int, input().split())

# Please write your code here.
# c시 d분 -> c-1시 d+60분
c = c-1
d = d+60

# d+60분 - b분
minute = d - b
if minute>= 60:
    minute -= 60
    c += 1
hr = c-a

result = hr*60 + minute
print(result)