N = int(input())
A = list(map(int, input().split()))
s = set()
for a in A:
    s.add(a)
    
print(len(s))