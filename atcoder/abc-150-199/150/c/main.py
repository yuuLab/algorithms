import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

 # 0からn-1までのリスト
lis = [x for x in range(1, N+1)]
permutations_lis = itertools.permutations(lis)# 全ての場合のリストを生成
p_num = -1
q_num = -1
for i, one_case in enumerate(permutations_lis): 
#     print(i, one_case)
    isMatchP = True
    isMatchQ = True
    for j, case in enumerate(one_case):
        if case != P[j]:
            isMatchP = False
        if case != Q[j]:
            isMatchQ = False
    if isMatchP:
        p_num = i+1
    if isMatchQ:
        q_num = i+1

print(abs(p_num - q_num))