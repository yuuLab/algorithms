A, B = map(str, input().split())

a_sum = 0
b_sum = 0
for i in range(len(A)):
    a_sum += int(A[i])
for i in range(len(B)):
    b_sum += int(B[i])
if a_sum < b_sum:
    print(b_sum)
else:
    print(a_sum)