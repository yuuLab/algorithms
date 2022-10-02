N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

completely_same = 0
same_num = 0

s = set()
for i in range(N):
    s.add(A[i])
    if A[i] == B[i]:
        completely_same += 1
        continue
        
for i in range(N):
    if B[i] in s and A[i] != B[i]:
        same_num += 1

print(completely_same)
print(same_num)