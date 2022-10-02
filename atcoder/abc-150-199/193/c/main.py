import math

N = int(input())

temp = 0
nums = set()
for i in range(2, N):
    if i**2 > N:
        break
    for j in range(2, N):
        if i**j > N:
            break
        nums.add(i**j)
print(N - len(nums))
  
'''
公式回答
N = int(input())
sq = int(N**0.5)
s = set()
for a in range(2, sq + 1):
    x = a * a
    while x <= N:
        s.add(x)
        x *= a
print(N - len(s))
'''