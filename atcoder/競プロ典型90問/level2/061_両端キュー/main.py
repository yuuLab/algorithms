from collections import deque

# 両端キュー

Q = int(input())

cards = deque()
for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        cards.appendleft(x)
    elif t == 2:
        cards.append(x)
    else:
        print(cards[x-1])