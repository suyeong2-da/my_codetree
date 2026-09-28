h, w = map(int, input().split())

b = (10000*w)/(h*h)

if b >= 25:
    print(int(b))
    print('Obesity')
else:
    print(int(b))