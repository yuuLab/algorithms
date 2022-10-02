S = input()
T = input()

len_s = len(S)
len_t = len(T)
ans = 10**4
for i in range(len_s - len_t + 1):
    tmp = 0
    for j in range(len_t):
        if S[i+j] != T[j]:
            tmp += 1
    ans = min(ans, tmp)

print(ans)