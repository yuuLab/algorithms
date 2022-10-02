from collections import deque

Q = int(input())
d = deque()

for i in range(Q):
    query = list(map(int, input().split()))
    if 1 == query[0]:
        x = query[1]
        c = query[2]
        d.append([x, c])
    else:
        c = query[1]
        output = 0
        while len(d):
            x, n = d.popleft()
            output += min(c, n)*x
            if c <= n:
                print(output)
                if c != n:
                    d.appendleft([x, n-c])
                break
            c -= n