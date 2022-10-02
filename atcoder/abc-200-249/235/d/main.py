from collections import deque

a, N = map(int, input().split())

def operate1(n: int, a: int):
    return n*a

def operate2(n: int):
    str_num = str(n)
    return int(str_num[-1] + str_num[:-1])


M = 1
while M <= N:
    M *= 10
    
# 初期化
d = [-1] * M
que = deque()
d[1] = 0
que.append(1)

while len(que):
    c = que.popleft()
    dc = d[c]
    
    op1 = operate1(c, a)
    if op1 < M and d[op1] == -1:
        d[op1] = dc + 1
        que.append(op1)
        
    if c >= 10 and c % 10 != 0:
        op2 = operate2(c)
        if op2 < M and d[op2] == -1:
            d[op2] = dc + 1
            que.append(op2)
        
print(d[N])