# 2進数をうまく活用する解法
# 高橋君がいまいる頂点の番号を 2 進法で表した文字列 T で管理することを考える
N, X = map(int, input().split())
S = input()

X = list(bin(int(X)))
for c in S:
    if c == "U":
        X.pop()
    elif c == "L":
        X.append("0")
    elif c == "R":
        X.append("1")
        
print(int("".join(X), 2))