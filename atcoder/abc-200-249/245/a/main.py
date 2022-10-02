a, b, c, d = map(int, input().split())

if a > c :
    print("Aoki")
elif a < c:
    print("Takahashi")
else:
    if b > d:
        print("Aoki")
    elif b < d:
        print("Takahashi")
    else:
        print("Takahashi")