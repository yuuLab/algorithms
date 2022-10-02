N = int(input())
result = 10**N - 9**N - 9**N + 8**N
ans = result % ((10**9) + 7)
print(ans)