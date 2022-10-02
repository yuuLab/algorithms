import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for i in range(N)]

nums = list(range(1,N))
for index in itertools.permutations(nums):
    print([0] + list(index))