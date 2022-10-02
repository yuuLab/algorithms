import itertools

N, M = map(int, input().split())

taka = []
aoki = [[0]*N for _ in range(N)]

# 後で順に調査するため一旦リストに保持1
for i in range(M):
    A, B = map(int, input().split())
    taka.append([A-1, B-1])
    
# 辺を張る
for i in range(M):
    C, D = map(int, input().split())
    aoki[C-1][D-1] = 1
    aoki[D-1][C-1] = 1


# 順列で全ての組み合わせを探索する。
nums = [i for i in range(N)]
patterns = itertools.permutations(nums, N)
ans = 'No'
for p in patterns:
    l = list(p)
    is_same = True
    for i in range(M):
        A, B = taka[i]
        C = l[A]
        D = l[B]
        if aoki[C][D] == 0:
            is_same = False
            break
    if is_same:
        ans = 'Yes'
        break
        
        
print(ans)  