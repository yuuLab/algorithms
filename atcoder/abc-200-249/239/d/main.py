import math

A, B, C, D = map(int, input().split())

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

winner = 'Aoki'
for i in range(A, B+1):
    can_win_t = True
    for j in range(C, D+1):
        if is_prime(i + j):
            can_win_t = False
            break
    if can_win_t:
        winner = 'Takahashi'
        break
print(winner)