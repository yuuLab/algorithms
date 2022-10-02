R, X, Y = map(int, input().split())
distance = (X**2 + Y**2)**0.5
if distance % R == 0 :
    print(int(distance//R))
elif distance < R:
    print(2)
else:
    print(int((distance//R) + 1))