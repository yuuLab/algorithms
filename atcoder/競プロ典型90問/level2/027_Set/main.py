N = int(input())

registed = set()
for i in range(1, N+1):
    s = input()
    if not s in registed:
        registed.add(s)
        print(i)
