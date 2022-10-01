N, L = map(int, input().split())

not_eat = N * (L - 1) + N * (N + 1) // 2

tmp_abs = float('INF')
ans = 0

for i in range(1, N+1):
    eat_i = not_eat - (L + i - 1)
    tmp = abs(not_eat - eat_i)
    if tmp < tmp_abs:
        ans = eat_i
        tmp_abs = tmp
        
print(ans)