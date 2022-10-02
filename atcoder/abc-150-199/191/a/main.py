V, T, S, D = map(int, input().split())

start = V * T
end = V * S
if start <= D <= end:
    print('No')
else :
    print('Yes')