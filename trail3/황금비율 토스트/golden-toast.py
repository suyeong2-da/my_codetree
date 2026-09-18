n, m = map(int, input().split())
s = input()

commands = []
for _ in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        commands.append((cmd[0],))
    else:
        commands.append((cmd[0], cmd[1]))

# Please write your code here.
# s_list = []
# for i in range(len(s)):
#     s_list.append(s[i])

# position = len(s_list)

# for i in range(m):
#     if commands[i][0] == 'L':
#         if position != 0:
#             position -= 1
#     elif commands[i][0] == 'R':
#         if position != len(s_list):
#             position += 1
#     elif commands[i][0] == 'D':
#         if position != len(s_list):
#             new = s_list[:position]
#             new.extend(s_list[position+1:])
#             s_list = new
#     elif commands[i][0] == 'P':
#         new = s_list[:position]
#         new.append(commands[i][1])
#         new.extend(s_list[position:])
#         position += 1
#         s_list = new


# print(*s_list, sep='')
left = list(s)
right = []

for i in range(m):
    if commands[i][0] == 'L':
        if left:
            right.append(left.pop())
    elif commands[i][0] == 'R':
        if right:
            left.append(right.pop())
    elif commands[i][0] == 'D':
        if right:
            right.pop()
    elif commands[i][0] == 'P':
        left.append(commands[i][1])

for i in range(len(right)):
    left.append(right.pop())

print(*left, sep='')