x, y = map(int, input().split())
if x == y:
    print(x)
elif x + y == 1:
    print(2)
elif x + y == 2:
    print(1)
elif x + y == 3:
    print(0)