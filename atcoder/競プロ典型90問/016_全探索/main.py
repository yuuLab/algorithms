n = int(input())

a, b, c = map(int,input().split())

num = 9999
for i in range(num):
    for j in range(num - i):
        k = (n - a*i - b*j) // c
        if a*i + b*j + c*k == n and k >= 0:
            num = min(num, i+j+k)

print(num)