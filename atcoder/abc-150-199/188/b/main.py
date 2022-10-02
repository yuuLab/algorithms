import numpy as np

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
array = np.array(A)*np.array(B)
dot = 0
for i in array:
    dot += i
if dot == 0:
    print('Yes')
else :
    print('No')