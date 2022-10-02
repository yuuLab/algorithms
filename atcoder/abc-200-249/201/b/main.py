N = int(input())

first = 0
first_name = ''
second = 0
ans = ''
for _ in range(N):
    S, T = input().split()
    if first < int(T):
        second = first
        ans = first_name
        first = int(T)
        first_name = S
    elif second < int(T):
        second = int(T)
        ans = S
print(ans)