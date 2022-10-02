def has_bit(n ,i):
    return n & (1<<i)

N, K = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
for bit in range(1<<N):
    char = [0] * 26
    for i in range(N):
        if has_bit(bit, i):
            for s in S[i]:
                char[ord(s)-97]+=1
    ans=max(ans,char.count(K))
    
print(ans)