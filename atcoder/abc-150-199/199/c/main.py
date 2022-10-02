N = int(input())
S = list(input())
S_before = S[:N]
S_after = S[N:]
Q = int(input())

for i in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if A <= N and B > N:
            s1 = S_before[A-1]
            s2 = S_after[B-1-N]
            S_before[A-1] = s2
            S_after[B-1-N] = s1
        elif B <= N:
            s1 = S_before[A-1]
            s2 = S_before[B-1]
            S_before[A-1] = s2
            S_before[B-1] = s1
        else:
            s1 = S_after[A-1-N]
            s2 = S_after[B-1-N]
            S_after[A-1-N] = s2
            S_after[B-1-N] = s1
    else:
        S_before, S_after = S_after, S_before
print(''.join(S_before) + ''.join(S_after))