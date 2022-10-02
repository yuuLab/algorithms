N, K = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(N)]

ans = K
friends.sort()
for friend in friends:
    if friend[1] <= ans:
        ans += friend[1]
print(ans)