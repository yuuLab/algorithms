N, D, S = map(int, input().split())
def check():
    X, Y = map(int, input().split())
    return X < S and Y > D

if any(check() for i in range(N)):
    print("Yes")
else:
    print("No")