n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.

new1 = []
for i in range(len(blocks)):
    if i < s1-1 or i > e1-1:
        new1.append(blocks[i])

new2 = []
for i in range(len(new1)):
    if i < s2-1 or i > e2-1:
        new2.append(new1[i])
        
print(len(new2), *new2, sep='\n')