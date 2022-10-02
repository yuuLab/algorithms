N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_max = max(A)
b_min = min(B)
ans = 0
for i in range(1, b_min+1):
    if a_max <= i and i <= b_min:
        ans += 1
print(ans)
    