N, X, T = map(int, input().split())

q, mod =  divmod(N, X)
if mod == 0:
    print(q*T)
else:
    print(q*T+T)