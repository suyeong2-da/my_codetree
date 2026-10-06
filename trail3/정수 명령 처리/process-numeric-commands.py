N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.

result = []
for i in range(N):
    if command[i] == "push":
        result.append(value[i])
    elif command[i] == "pop":
        print(result.pop())
    elif command[i] == "size":
        print(len(result))
    elif command[i] == "empty":
        if len(result)==0: print(1)
        else: print(0)
    elif command[i] == "top":
        print(result[-1])

    
