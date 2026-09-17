N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
result = []

for i in range(N):
    if command[i] == 'push_front':
        r = result
        result = []
        result.append(A[i])
        result.extend(r)
    elif command[i] == 'push_back':
        result.append(A[i])
    elif command[i] == 'pop_front':
        print(result.pop(0))
    elif command[i] == 'pop_back':
        print(result.pop())
    elif command[i] == 'size':
        print(len(result))
    elif command[i] == 'empty':
        if len(result)==0:
            print(1)
        else:
            print(0)
    elif command[i] == 'front':
        print(result[0])
    elif command[i] == 'back':
        print(result[-1])