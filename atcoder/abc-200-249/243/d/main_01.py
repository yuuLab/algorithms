# 計算量を事前に削減し、位置を愚直に計算する解法
N, X = map(int, input().split())
S = input()

T = []
# Uの後にLもしくはRが続く場合は、元の位置に戻るのでスキップして計算量を減らす
for s in S:
    if s == "U" and len(T) > 0 and (T[-1] == "L" or T[-1] == "R"):
        T.pop()
    else:
        T.append(s)
        
for t in T:
    if t == "U":
        X = X//2
    elif t == "L":
        X = X*2
    elif t == "R":
        X = X*2 + 1
        
print(X)