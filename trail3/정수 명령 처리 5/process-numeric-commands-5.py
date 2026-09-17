N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
result = []

for i in range(N):
    if command[i] =="push_back":
        result.append(num[i])
    elif command[i] =="pop_back":
        result.pop()
    elif command[i] =="size":
        print(len(result))
    elif command[i] =="get":
        print(result[num[i]-1])
