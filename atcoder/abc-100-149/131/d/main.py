N = int(input())
tasks = []
for i in range(N):
    A, B = map(int, input().split())
    tasks.append([B, A])

tasks.sort()

now = 0
ans = 'Yes'
for i in range(N):
    deadline, cost = tasks[i]
    if cost + now > deadline:
        ans = 'No'
        break
    now += cost
    
print(ans)