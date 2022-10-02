S1, S2, S3 = map(str, input().split())
T1, T2, T3 = map(str, input().split())

A = ["R G B", "G B R", "B R G"]
S = input()
T = input()
print("Yes" if (S in A) == (T in A) else "No")