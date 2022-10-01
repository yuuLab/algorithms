N = int(input())
A = list(map(int, (input().split())))

'''
山iに降った雨をxiとすると
xi + xi+1 = 2Ai

x1+x2=A1*2
x2+x3=A2*2
x3+x1=A3*2
奇数行を足し、偶数行を引くと以下の式になる
x1 = A1-A2*A3-...+An
'''

total = sum(A)
x1 = 0
for i in range(N):
    if i%2 == 0:
        x1 += A[i]
    else:
        x1 -= A[i]

ans = [x1]
for i in range(1, N):
    a = 2 * A[i-1] - ans[i-1]
    ans.append(a)


print(*ans)