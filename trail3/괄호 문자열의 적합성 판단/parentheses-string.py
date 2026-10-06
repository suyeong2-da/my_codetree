str = input()

# Please write your code here.
arr = []
flag = True

for s in str:
    if s == "(":
        arr.append(s)

    elif s == ")":
        if len(arr) > 0:
            arr.pop()
        else:
            flag = False
            break

if len(arr) > 0:
    flag = False

if flag:
    print("Yes")
else:
    print("No")