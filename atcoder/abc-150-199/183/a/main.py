def Relu(x):
    if x >= 0:
        return x
    else:
        return 0

X = int(input())
print(Relu(X))