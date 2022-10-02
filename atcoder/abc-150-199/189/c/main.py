import numpy as np

N = int(input())
orange = np.array(list(map(int, input().split())), dtype=np.int64)
array = np.arange(1, N+1)
ans = max((np.minimum.accumulate(orange[i:])*array[:N-i]).max() for i in range(N))
print(ans)

'''
# これはTLE
#
# N = int(input())
# oranges = [list(map(int, input().split()))][0]
# ans = 0
# for l in range(N):
#     for r in range(l+1, N+1):
#         s = (min(oranges[l:r]) * len(oranges[l:r]))
#         if(s > ans):
#             ans = s
# print(ans)
'''