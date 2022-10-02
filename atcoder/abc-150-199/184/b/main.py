N, X = map(int, input().split())
S = input()

score = X
for i in range(N):
    if S[i] == 'o':
        score += 1
    else:
        score_kari = score - 1
        score = max(0, score_kari)
print(score)