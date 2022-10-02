n = int(input())
A = list(map(int, input().split()))

a1 = 0
a2 = 0
for i in range(n):
    a1 += A[i]**2
    a2 += A[i]
    
print(n*a1 - a2**2)