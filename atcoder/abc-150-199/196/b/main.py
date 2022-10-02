X = input()

idx = -1
for i in range(len(X)):
    if X[i] == '.':
        idx = i
if idx == -1:
    print(X)
else:
    print(X[:idx])