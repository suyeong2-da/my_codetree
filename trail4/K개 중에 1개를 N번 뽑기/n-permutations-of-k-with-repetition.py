K, N = map(int, input().split())

# Please write your code here.
# 중복 순열
num = [n for n in range(1, K+1)]
path = ['']*N

def perm(level):
    if level == N:
        print(*path)
        return

    for i in range(K):
        path[level] = num[i]
        perm(level+1)

perm(0)