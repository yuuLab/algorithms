N = [int(x) for x in list(input())]

SUM = 0
length = len(N)
amari_1 = False
amari_2 = False
for n in N:
    SUM += n
    if n % 3 == 1:
        amari_1 = True
    if n % 3 == 2:
        amari_2 = True

if SUM % 3 == 0:
    print(0)
elif SUM % 3 == 1:
    if length == 1:
        print(-1)
    elif amari_1:
        print(1)
    elif length == 2:
        print(-1)
    else:
        print(2)
else:
    if length == 1:
        print(-1)
    elif amari_2:
        print(1)
    elif length == 2:
        print(-1)
    else:
        print(2)