V, A, B, C = map(int, input().split())

S = A + B + C
mod = V % S

if mod < A:
    print('F')
elif mod < A + B:
    print('M')
else:
    print('T')