S = list(map(str, input()))

ans = S[0]
flag = True
for i in range(len(S)):
    if(ans != S[i]):
        flag = False
msg = "Won" if flag else "Lost"
print(msg)