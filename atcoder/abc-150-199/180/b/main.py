N = int(input())
X = list(map(int, input().split()))

manhattan = 0
euclid = 0
chebyshev = []

for x in X:
    manhattan += abs(x)
    euclid += x**2
    chebyshev.append(abs(x))

    
print(manhattan)
print(euclid**0.5)
print(max(chebyshev))