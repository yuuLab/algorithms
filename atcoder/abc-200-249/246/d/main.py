N = int(input())

def func(i, j):
    return i**3 + (i**2)*j + i*(j**2) + j**3

ans = 10**18
j = 10**6

for i in range(10**6):
    while func(i, j) >= N and j >= 0:
        ans = min(ans, func(i, j))
        j -= 1
        
print(ans)